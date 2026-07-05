"""
Optimized RAG Chatbot - Memory Efficient!
Uses TinyLlama with batch processing
"""

import requests
import json
import numpy as np
from typing import List, Dict
import time

class OptimizedRAGChatbot:
    def __init__(self, model_name="tinyllama"):
        self.model_name = model_name
        self.ollama_url = "http://localhost:11434/api/generate"
        self.documents = []
        self.embeddings = []
        self.chunk_size = 300  # Smaller chunks
        self.chunk_overlap = 30
        self.max_context_length = 200  # Limit context size
        
        print(f"🤖 Optimized RAG with {model_name}")
        print(f"📊 Memory efficient mode: ON")
    
    def add_document(self, text: str, metadata: Dict = None):
        """Add document with smaller chunks"""
        chunks = self._chunk_text(text)
        
        for chunk in chunks:
            self.documents.append({
                'text': chunk[:200],  # Truncate long chunks
                'metadata': metadata or {}
            })
        
        # Simple embedding (no heavy computation)
        self._generate_simple_embeddings()
        
        print(f"✅ Added {len(chunks)} chunks")
        print(f"📚 Total: {len(self.documents)} chunks")
    
    def _chunk_text(self, text: str) -> List[str]:
        """Split text into smaller chunks"""
        words = text.split()
        chunks = []
        current_chunk = []
        current_size = 0
        
        for word in words:
            current_chunk.append(word)
            current_size += len(word) + 1
            
            if current_size > self.chunk_size:
                chunks.append(' '.join(current_chunk))
                current_chunk = []
                current_size = 0
        
        if current_chunk:
            chunks.append(' '.join(current_chunk))
        
        return chunks
    
    def _generate_simple_embeddings(self):
        """Simple TF-IDF style embeddings"""
        self.embeddings = []
        
        for doc in self.documents:
            # Create simple word frequency embedding
            words = doc['text'].lower().split()
            embedding = np.zeros(50)  # Smaller dimension
            
            for word in words[:20]:  # Limit words per document
                hash_val = abs(hash(word)) % 50
                embedding[hash_val] += 1
            
            # Normalize
            norm = np.linalg.norm(embedding)
            if norm > 0:
                embedding = embedding / norm
            
            self.embeddings.append(embedding)
    
    def _get_query_embedding(self, query: str) -> np.ndarray:
        """Simple query embedding"""
        words = query.lower().split()
        embedding = np.zeros(50)
        
        for word in words[:10]:  # Limit query words
            hash_val = abs(hash(word)) % 50
            embedding[hash_val] += 1
        
        norm = np.linalg.norm(embedding)
        if norm > 0:
            embedding = embedding / norm
        
        return embedding
    
    def retrieve(self, query: str, top_k: int = 2) -> List[Dict]:
        """Retrieve only top relevant chunks"""
        if not self.documents:
            return []
        
        query_embedding = self._get_query_embedding(query)
        
        # Compute similarities
        scores = []
        for i, doc_embedding in enumerate(self.embeddings):
            similarity = np.dot(query_embedding, doc_embedding)
            scores.append((i, similarity))
        
        # Sort and return top_k
        scores.sort(key=lambda x: x[1], reverse=True)
        
        results = []
        for i, score in scores[:top_k]:
            results.append({
                'text': self.documents[i]['text'],
                'score': float(score),
                'metadata': self.documents[i]['metadata']
            })
        
        return results
    
    def ask(self, question: str) -> Dict:
        """Answer with minimal context"""
        # Retrieve relevant chunks
        results = self.retrieve(question)
        
        if not results:
            return {
                'question': question,
                'answer': "I need more information. Please add documents.",
                'context': [],
                'sources': []
            }
        
        # Limit context to avoid memory issues
        context = results[0]['text']  # Only use top result
        if len(context) > 200:
            context = context[:200] + "..."
        
        # Generate response with TinyLlama (lightweight prompt)
        prompt = f"""Context: {context}

Question: {question}

Short answer:"""
        
        try:
            response = requests.post(
                self.ollama_url,
                json={
                    "model": self.model_name,
                    "prompt": prompt,
                    "stream": False,
                    "temperature": 0.5,  # Lower temperature = faster
                    "max_tokens": 50,    # Shorter responses
                    "options": {
                        "num_ctx": 512   # Smaller context window
                    }
                },
                timeout=30
            )
            
            if response.status_code == 200:
                answer = response.json()['response'].strip()
                # Truncate if too long
                if len(answer) > 200:
                    answer = answer[:200] + "..."
            else:
                answer = "Error generating response"
                
        except Exception as e:
            answer = f"Error: {str(e)[:100]}"
        
        return {
            'question': question,
            'answer': answer,
            'context': [context],
            'sources': [r.get('metadata', {}).get('source', 'Unknown') for r in results[:1]]
        }

# Test with sample
if __name__ == "__main__":
    print("🧪 Testing Optimized RAG...")
    
    # Sample document
    doc = """
    Artificial Intelligence is the simulation of human intelligence processes by machines.
    Machine Learning enables systems to learn from data without explicit programming.
    Deep Learning uses neural networks with multiple layers for pattern recognition.
    Natural Language Processing helps computers understand human language.
    Computer Vision allows machines to interpret visual information.
    Reinforcement Learning trains agents through rewards and punishments.
    """
    
    bot = OptimizedRAGChatbot("tinyllama")
    bot.add_document(doc, {'source': 'AI Basics'})
    
    questions = [
        "What is AI?",
        "What is Machine Learning?",
        "What is Deep Learning?"
    ]
    
    for q in questions:
        print(f"\n❓ {q}")
        result = bot.ask(q)
        print(f"🤖 {result['answer']}")
        print("-" * 40)
    
    print("\n✅ Test complete! Memory optimized.")
