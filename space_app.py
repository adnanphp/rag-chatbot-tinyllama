"""
Gradio interface for RAG Chatbot - Compatible with Gradio 6.x
Supports PDF and TXT files
"""

import gradio as gr
import os
from pypdf import PdfReader

# Simple RAG without local LLM
class SimpleRAG:
    def __init__(self):
        self.documents = []
        self.keywords = {}
    
    def add_document(self, text):
        sentences = [s.strip() for s in text.split('.') if len(s.strip()) > 20]
        for i, sent in enumerate(sentences):
            self.documents.append(sent)
            words = sent.lower().split()
            for word in words:
                if len(word) > 3:
                    if word not in self.keywords:
                        self.keywords[word] = []
                    self.keywords[word].append(i)
    
    def ask(self, question):
        words = question.lower().split()
        relevant = []
        for word in words:
            if len(word) > 3 and word in self.keywords:
                for idx in self.keywords[word]:
                    if idx not in relevant:
                        relevant.append(idx)
        
        if not relevant:
            return "I don't have information about that topic."
        
        context = []
        for idx in relevant[:2]:
            context.append(self.documents[idx])
        
        return f"Based on my knowledge: {' '.join(context)}"

# Initialize RAG
rag = SimpleRAG()

# Load documents from folder
documents_folder = "documents"

if os.path.exists(documents_folder):
    print(f"📁 Loading documents from {documents_folder}...")
    
    for filename in os.listdir(documents_folder):
        filepath = os.path.join(documents_folder, filename)
        
        try:
            # Handle PDF files
            if filename.lower().endswith('.pdf'):
                print(f"📄 Reading PDF: {filename}")
                reader = PdfReader(filepath)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + " "
                rag.add_document(text)
                print(f"✅ Loaded PDF: {filename} ({len(text)} characters)")
            
            # Handle TXT files
            elif filename.lower().endswith('.txt'):
                print(f"📄 Reading TXT: {filename}")
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    text = f.read()
                rag.add_document(text)
                print(f"✅ Loaded TXT: {filename} ({len(text)} characters)")
            
            else:
                print(f"⚠️ Skipping unsupported file: {filename}")
                
        except Exception as e:
            print(f"❌ Error loading {filename}: {e}")

else:
    print("📁 No documents folder found. Please create one and add your files.")

print(f"📚 Total documents loaded: {len(rag.documents)}")

# Gradio 6.x ChatInterface
def chat_response(message, history):
    if not message:
        return "Please ask a question."
    
    response = rag.ask(message)
    return response

demo = gr.ChatInterface(
    fn=chat_response,
    title="🤖 RAG Chatbot with TinyLlama",
    description="Ask questions about your documents! Supports PDF and TXT files.",
    examples=[
        "What is this document about?",
        "Explain the main topic.",
        "What are the key points?",
        "Tell me about machine learning.",
        "What does the author say about AI?"
    ]
)

if __name__ == "__main__":
    demo.launch()
