"""
Gradio interface for RAG Chatbot on Hugging Face Spaces
"""

import gradio as gr
import requests
import json
import os

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
        
        # Get top 2 relevant sentences
        context = []
        for idx in relevant[:2]:
            context.append(self.documents[idx])
        
        return f"Based on my knowledge: {' '.join(context)}"

# Initialize RAG
rag = SimpleRAG()

# Sample knowledge
knowledge = """
Artificial Intelligence is the simulation of human intelligence processes by machines.
Machine Learning enables systems to learn from data without explicit programming.
Deep Learning uses neural networks with multiple layers for pattern recognition.
Natural Language Processing helps computers understand human language.
Computer Vision allows machines to interpret visual information.
Reinforcement Learning trains agents through rewards and punishments.
Transfer Learning applies knowledge from one task to another.
"""
rag.add_document(knowledge)

def chat_with_rag(message, history):
    """Chat function for Gradio"""
    if not message:
        return "Please ask a question."
    
    response = rag.ask(message)
    return response

# Create Gradio interface
with gr.Blocks(title="RAG Chatbot", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🤖 RAG Chatbot with TinyLlama
    
    Ask questions about AI, Machine Learning, Deep Learning, NLP, Computer Vision, and more!
    
    *Powered by TinyLlama and RAG (Retrieval-Augmented Generation)*
    """)
    
    with gr.Row():
        with gr.Column(scale=2):
            chatbot = gr.Chatbot(
                height=400,
                label="Chat History"
            )
            msg = gr.Textbox(
                label="Ask a question",
                placeholder="Type your question here...",
                lines=2
            )
            with gr.Row():
                submit_btn = gr.Button("Send", variant="primary")
                clear_btn = gr.Button("Clear")
    
    with gr.Row():
        with gr.Column():
            gr.Examples(
                examples=[
                    "What is Artificial Intelligence?",
                    "What is Machine Learning?",
                    "What is Deep Learning?",
                    "What is Natural Language Processing?",
                    "What is Computer Vision?",
                    "What is Reinforcement Learning?"
                ],
                inputs=msg
            )
    
    def respond(message, chat_history):
        if not message:
            return "", chat_history
        
        bot_response = chat_with_rag(message, chat_history)
        chat_history.append((message, bot_response))
        return "", chat_history
    
    submit_btn.click(
        respond,
        inputs=[msg, chatbot],
        outputs=[msg, chatbot]
    )
    
    msg.submit(
        respond,
        inputs=[msg, chatbot],
        outputs=[msg, chatbot]
    )
    
    clear_btn.click(
        lambda: None,
        inputs=None,
        outputs=chatbot,
        js="() => { document.querySelector('#chatbot').innerHTML = ''; }"
    )

if __name__ == "__main__":
    demo.launch()
