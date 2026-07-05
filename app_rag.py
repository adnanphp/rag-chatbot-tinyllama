"""
FastAPI for RAG Chatbot
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from rag_optimized import OptimizedRAGChatbot
import os

app = FastAPI(
    title="RAG Chatbot API",
    description="Ask questions based on your documents using TinyLlama",
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
print("🤖 Initializing RAG Chatbot API...")
chatbot = OptimizedRAGChatbot("tinyllama")

# Load sample documents if they exist
if os.path.exists("documents"):
    for filename in os.listdir("documents"):
        if filename.endswith('.txt'):
            with open(f"documents/{filename}", 'r') as f:
                text = f.read()
                chatbot.add_document(text, {'source': filename})
                print(f"✅ Loaded: {filename}")

class Question(BaseModel):
    question: str

class Document(BaseModel):
    text: str
    metadata: Optional[dict] = {}

@app.get("/")
async def root():
    return {
        "message": "RAG Chatbot API",
        "status": "running",
        "model": "tinyllama",
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
        "model": "tinyllama",
        "documents": len(chatbot.documents),
        "chunks": len(chatbot.documents)
    }

@app.post("/ask")
async def ask_question(question: Question):
    """Ask a question and get an answer"""
    if not chatbot.documents:
        raise HTTPException(
            status_code=400,
            detail="No documents loaded. Add documents first."
        )
    
    result = chatbot.ask(question.question)
    return result

@app.post("/add_document")
async def add_document(doc: Document):
    """Add a document to the knowledge base"""
    try:
        chatbot.add_document(doc.text, doc.metadata)
        return {
            "message": "Document added",
            "total_chunks": len(chatbot.documents)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/documents")
async def list_documents():
    """List all documents in the knowledge base"""
    sources = set()
    for doc in chatbot.documents:
        source = doc.get('metadata', {}).get('source', 'Unknown')
        sources.add(source)
    
    return {
        "count": len(chatbot.documents),
        "sources": list(sources)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
