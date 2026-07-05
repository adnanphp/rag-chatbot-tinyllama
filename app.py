"""
FastAPI application for RAG Chatbot
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import os
from rag_pipeline import RAGChatbot

# Initialize FastAPI app
app = FastAPI(
    title="RAG Chatbot API",
    description="Document Q&A using TinyLlama and RAG",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize chatbot
print("🤖 Initializing RAG Chatbot...")
chatbot = RAGChatbot()

# Load documents if available
DOCUMENTS_DIR = "./documents"
if os.path.exists(DOCUMENTS_DIR):
    for filename in os.listdir(DOCUMENTS_DIR):
        if filename.endswith('.txt') or filename.endswith('.md'):
            with open(os.path.join(DOCUMENTS_DIR, filename), 'r') as f:
                text = f.read()
                chatbot.add_document(text, {'source': filename})
                print(f"✅ Loaded: {filename}")
else:
    print("📁 No documents directory found. Use /add_document to add knowledge.")

class Question(BaseModel):
    question: str
    top_k: Optional[int] = 3

class Document(BaseModel):
    text: str
    metadata: Optional[dict] = {}

class ChatResponse(BaseModel):
    question: str
    answer: str
    context: List[str]
    sources: List[str]
    relevance_scores: List[float]

@app.get("/")
async def root():
    return {
        "message": "RAG Chatbot API",
        "status": "running",
        "model": chatbot.model_name,
        "documents": len(chatbot.documents),
        "endpoints": [
            "/",
            "/health",
            "/ask",
            "/add_document",
            "/documents"
        ]
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "model": chatbot.model_name,
        "documents": len(chatbot.documents),
        "chunks": len(chatbot.documents)
    }

@app.post("/ask", response_model=ChatResponse)
async def ask_question(question: Question):
    """
    Ask a question and get an answer based on your documents
    """
    if not chatbot.documents:
        raise HTTPException(
            status_code=400,
            detail="No documents loaded. Please add documents first."
        )
    
    result = chatbot.ask(question.question)
    
    return ChatResponse(
        question=result['question'],
        answer=result['answer'],
        context=result['context'],
        sources=result['sources'],
        relevance_scores=result['relevance_scores']
    )

@app.post("/add_document")
async def add_document(doc: Document):
    """
    Add a document to the knowledge base
    """
    try:
        chatbot.add_document(doc.text, doc.metadata)
        return {
            "message": "Document added successfully",
            "total_documents": len(chatbot.documents),
            "total_chunks": len(chatbot.documents)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/documents")
async def list_documents():
    """
    List all documents in the knowledge base
    """
    if not chatbot.documents:
        return {"documents": [], "count": 0}
    
    # Get unique sources
    sources = set()
    for doc in chatbot.documents:
        source = doc.get('metadata', {}).get('source', 'Unknown')
        sources.add(source)
    
    return {
        "count": len(chatbot.documents),
        "sources": list(sources),
        "documents": chatbot.documents[:10]  # Return first 10 for preview
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
