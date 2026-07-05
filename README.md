---
title: RAG Chatbot with TinyLlama
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: "4.8.0"
python_version: "3.12"
app_file: space_app.py
pinned: false
---

# 🤖 RAG Chatbot with TinyLlama

[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Space-yellow)](https://huggingface.co/spaces/adnanphp/rag-chatbot-tinyllama)
[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue)](https://github.com/adnanphp/rag-chatbot-tinyllama)
[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://python.org)

## 📋 Overview

A **Retrieval-Augmented Generation (RAG) Chatbot** that answers questions based on your documents. Built with **TinyLlama**, **FastAPI**, and **Gradio**.

### 🎯 Features

- 📄 **Document ingestion** - Add text documents as knowledge
- 🔍 **Semantic search** - Find relevant information
- 🤖 **LLM generation** - Answers using TinyLlama
- 🌐 **REST API** - FastAPI endpoints
- 🎨 **Web UI** - Gradio interface

## 🌐 Live Demo

| Platform | URL | Status |
|----------|-----|--------|
| **Hugging Face Spaces** | https://huggingface.co/spaces/adnanphp/rag-chatbot-tinyllama | ✅ Live |
| **Local API** | http://localhost:8000 | ✅ Running |

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **TinyLlama** | LLM for generation |
| **FAISS** | Vector search |
| **FastAPI** | REST API |
| **Gradio** | Web interface |

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/adnanphp/rag-chatbot-tinyllama.git
cd rag-chatbot-tinyllama

# Install dependencies
pip install -r requirements.txt

# Run API
python app_rag.py

# Or run Gradio UI
python space_app.py
📁 Project Structure
text
rag-chatbot-tinyllama/
├── rag_optimized.py     # RAG pipeline
├── app_rag.py          # FastAPI app
├── space_app.py        # Gradio UI
├── documents/          # Knowledge base
├── requirements.txt    # Dependencies
└── README.md           # Documentation
📊 API Endpoints
Method	Endpoint	Description
GET	/	Root endpoint
GET	/health	Health check
POST	/ask	Ask a question
POST	/add_document	Add knowledge
GET	/documents	List documents
📝 License
MIT

👨‍💻 Author
Adnan - GitHub

🔗 Live Demo: https://huggingface.co/spaces/adnanphp/rag-chatbot-tinyllama
