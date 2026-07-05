"""
RAG (Retrieval-Augmented Generation) Chatbot
Using TinyLlama + LangChain + FAISS
"""

import os
import requests
import json
from typing import List, Dict
import numpy as np

class RAGChatbot:
    def __init__(self, model_name="tinyllama"):
        """
        Initialize the RAG chatbot with Ollama model
        """
        self.model_name = model_name
        self.ollama_url = "http://localhost:11434/api/generate"
        self.documents = []
        self.embeddings = []
        self.chunk_size = 500
        self.chunk_overlap = 50
        
        print(f"🤖 RAG Chatbot initialized with model: {model_name}")
    
    def add_document(self, text: str, metadata: Dict = None):
        """
        Add a document to the knowledge base
        """
        # Split text into chunks
        chunks = self._chunk_text(text)
        
        for chunk in chunks:
            self.documents.append({
                'text': chunk,
                'metadata': metadata or {}
            })
        
        # Generate embeddings for chunks
        self._generate_embeddings()
        
        print(f"✅ Added {len(chunks)} chunks from document")
        print(f"📚 Total chunks: {len(self.documents)}")
    
    def _chunk_text(self, text: str) -> List[str]:
        """
        Split text into overlapping chunks
        """
        chunks = []
        start = 0
        text_length = len(text)
        
        while start < text_length:
            end = min(start + self.chunk_size, text_length)
            
            # Try to end at a sentence boundary
            if end < text_length:
                # Look for period, question mark, or exclamation
                for i in range(end, max(start, end - 100), -1):
                    if text[i] in '.!?':
                        end = i + 1
                        break
            
            chunks.append(text[start:end])
            start = end - self.chunk_overlap
        
        return chunks
    
    def _generate_embeddings(self):
        """
        Generate embeddings for all documents
        Using a simple approach since we're using TinyLlama
        """
        # For simplicity, we'll use a mock embedding approach
        # In production, use sentence-transformers or similar
        self.embeddings = []
        for doc in self.documents:
            # Simple embedding based on word frequency
            words = doc['text'].lower().split()
            embedding = np.zeros(100)  # 100-dim vector
            
            for word in words:
                # Hash word to a vector
                hash_val = hash(word) % 100
                embedding[abs(hash_val)] += 1
            
            # Normalize
            if np.linalg.norm(embedding) > 0:
                embedding = embedding / np.linalg.norm(embedding)
            
            self.embeddings.append(embedding)
    
    def _get_embedding(self, text: str) -> np.ndarray:
        """
        Get embedding for a query
        """
        words = text.lower().split()
        embedding = np.zeros(100)
        
        for word in words:
            hash_val = hash(word) % 100
            embedding[abs(hash_val)] += 1
        
        if np.linalg.norm(embedding) > 0:
            embedding = embedding / np.linalg.norm(embedding)
        
        return embedding
    
    def retrieve(self, query: str, top_k: int = 3) -> List[Dict]:
        """
        Retrieve most relevant document chunks for a query
        """
        if not self.documents:
            return []
        
        query_embedding = self._get_embedding(query)
        
        # Compute similarity scores
        scores = []
        for i, doc_embedding in enumerate(self.embeddings):
            similarity = np.dot(query_embedding, doc_embedding)
            scores.append((i, similarity))
        
        # Sort by similarity (descending)
        scores.sort(key=lambda x: x[1], reverse=True)
        
        # Return top_k results
        results = []
        for i, score in scores[:top_k]:
            results.append({
                'text': self.documents[i]['text'],
                'score': float(score),
                'metadata': self.documents[i]['metadata']
            })
        
        return results
    
    def generate(self, prompt: str, context: str = "") -> str:
        """
        Generate a response using TinyLlama
        """
        # Prepare the prompt with context
        full_prompt = f"""Context: {context}

Question: {prompt}

Answer based on the context above. If you don't know, say "I don't have enough information to answer that."

Answer:"""
        
        try:
            response = requests.post(
                self.ollama_url,
                json={
                    "model": self.model_name,
                    "prompt": full_prompt,
                    "stream": False,
                    "temperature": 0.7,
                    "max_tokens": 200
                },
                timeout=60
            )
            
            if response.status_code == 200:
                return response.json()['response'].strip()
            else:
                return f"Error: {response.status_code} - {response.text}"
                
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def ask(self, question: str) -> Dict:
        """
        Ask a question and get a response with context
        """
        # Retrieve relevant context
        results = self.retrieve(question)
        
        if not results:
            return {
                'question': question,
                'answer': "No documents available. Please add some documents first.",
                'context': [],
                'sources': []
            }
        
        # Combine context
        context = "\n\n".join([r['text'] for r in results])
        
        # Generate answer
        answer = self.generate(question, context)
        
        return {
            'question': question,
            'answer': answer,
            'context': [r['text'] for r in results],
            'sources': [r.get('metadata', {}).get('source', 'Unknown') for r in results],
            'relevance_scores': [r['score'] for r in results]
        }

# Example usage
if __name__ == "__main__":
    print("🧪 Testing RAG Chatbot...")
    
    # Create chatbot
    bot = RAGChatbot()
    
    # Add sample document
    sample_text = """
    Machine Learning is a subset of artificial intelligence that enables systems to learn and improve from experience without being explicitly programmed.
    
    Deep Learning is a subset of machine learning that uses neural networks with multiple layers to learn representations of data.
    
    Natural Language Processing is a field of AI that focuses on the interaction between computers and human language.
    
    Computer Vision is a field of AI that enables computers to interpret and understand visual information from the world.
    
    Reinforcement Learning is a type of machine learning where an agent learns to make decisions by taking actions in an environment to maximize cumulative reward.
    """
    
    bot.add_document(sample_text, {'source': 'AI Basics'})
    
    # Ask questions
    questions = [
        "What is Machine Learning?",
        "What is Deep Learning?",
        "What is NLP?",
        "What is Computer Vision?"
    ]
    
    for q in questions:
        print(f"\n❓ Question: {q}")
        result = bot.ask(q)
        print(f"🤖 Answer: {result['answer']}")
        print(f"📊 Sources: {result['sources']}")
        print("-" * 50)
    
    print("\n✅ RAG Chatbot test complete!")
