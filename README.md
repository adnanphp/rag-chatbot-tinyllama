---
title: RAG Chatbot with TinyLlama
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: "4.44.1"
python_version: "3.10"
app_file: space_app.py
pinned: false
---

# 🤖 RAG Chatbot with TinyLlama

[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Space-yellow)](https://huggingface.co/spaces/adnanphp/rag-chatbot-tinyllama)
[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue)](https://github.com/adnanphp/rag-chatbot-tinyllama)
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)

> **A lightweight Retrieval-Augmented Generation (RAG) chatbot that combines semantic retrieval with TinyLlama to answer questions from a custom knowledge base.**

## 🚀 Live Demo

**Hugging Face Space:**
https://huggingface.co/spaces/adnanphp/rag-chatbot-tinyllama

**GitHub Repository:**
https://github.com/adnanphp/rag-chatbot-tinyllama

---

## 📋 Overview

This project implements an end-to-end **Retrieval-Augmented Generation (RAG)** chatbot using **TinyLlama** for text generation and **FAISS** for semantic vector search.

The system retrieves relevant information from a collection of documents and provides that context to TinyLlama before generating an answer.

### 🔄 RAG Workflow

```text
User Question
      │
      ▼
Query Processing
      │
      ▼
FAISS Semantic Search
      │
      ▼
Relevant Documents
      │
      ▼
Retrieved Context
      │
      ▼
TinyLlama
      │
      ▼
Generated Answer
```

---

## ✨ Features

* 📄 **Document Ingestion** — Add documents to the knowledge base
* 🔍 **Semantic Search** — Retrieve relevant information using vector search
* 🤖 **TinyLlama Generation** — Generate answers using a lightweight LLM
* 🧠 **RAG Pipeline** — Combine retrieval with language generation
* ⚡ **FAISS Vector Search** — Efficient similarity search
* 🌐 **FastAPI REST API** — Access the chatbot programmatically
* 🎨 **Gradio Web UI** — Interactive chatbot interface
* 🤗 **Hugging Face Deployment** — Publicly accessible Gradio application

---

## 🧠 Architecture

```text
                  ┌─────────────────┐
                  │  User Question  │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Query Processing│
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  FAISS Search   │
                  │ Semantic Search │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Relevant Context│
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │    TinyLlama    │
                  │  Text Generation│
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │     Answer      │
                  └─────────────────┘
```

---

## 🛠️ Tech Stack

| Technology              | Purpose                  |
| ----------------------- | ------------------------ |
| **Python**              | Application development  |
| **TinyLlama**           | LLM for text generation  |
| **FAISS**               | Vector similarity search |
| **FastAPI**             | REST API                 |
| **Gradio**              | Web interface            |
| **Hugging Face Spaces** | Application deployment   |

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/adnanphp/rag-chatbot-tinyllama.git
cd rag-chatbot-tinyllama
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI Application

```bash
python app_rag.py
```

The API will be available at:

```text
http://localhost:8000
```

### 4. Run the Gradio Interface

```bash
python space_app.py
```

The Gradio application will start locally.

---

## 📡 REST API

The FastAPI application provides the following endpoints:

| Method | Endpoint        | Description    |
| ------ | --------------- | -------------- |
| `GET`  | `/`             | Root endpoint  |
| `GET`  | `/health`       | Health check   |
| `POST` | `/ask`          | Ask a question |
| `POST` | `/add_document` | Add a document |
| `GET`  | `/documents`    | List documents |

### Example Request

```bash
curl -X POST "http://localhost:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"question":"What information is available in the knowledge base?"}'
```

---

## 📁 Project Structure

```text
rag-chatbot-tinyllama/
│
├── documents/
│   └──              # Knowledge-base documents
│
├── rag_optimized.py # RAG pipeline
├── app_rag.py       # FastAPI application
├── space_app.py     # Gradio application
│
├── requirements.txt # Python dependencies
├── README.md        # Project documentation
└── LICENSE          # MIT License
```

---

## 🔍 How RAG Works

The chatbot follows a retrieval-then-generation approach.

### Step 1 — Document Ingestion

Documents are added to the knowledge base.

### Step 2 — Semantic Retrieval

FAISS searches the vector index to identify information relevant to the user's question.

### Step 3 — Context Construction

The retrieved information is provided as context to the language model.

### Step 4 — Answer Generation

TinyLlama uses the retrieved context to generate the final response.

```text
Documents
    │
    ▼
Vector Index
    │
    │
Question ───────► Semantic Search
                         │
                         ▼
                  Relevant Context
                         │
                         ▼
                     TinyLlama
                         │
                         ▼
                       Answer
```

---

## 🎯 Key Concepts Demonstrated

This project demonstrates practical experience with:

* Retrieval-Augmented Generation (RAG)
* Large Language Models (LLMs)
* Semantic search
* Vector similarity search
* FAISS
* Prompt-based context retrieval
* FastAPI
* REST API development
* Gradio
* Hugging Face Spaces
* LLM application deployment

---

## 💡 Why RAG?

A traditional LLM generates responses primarily from knowledge learned during model training.

RAG introduces an external knowledge source:

```text
Traditional LLM

Question ─────► LLM ─────► Answer


RAG

Question
    │
    ▼
Retriever
    │
    ▼
Relevant Context
    │
    ▼
TinyLlama
    │
    ▼
Answer
```

This allows the chatbot to answer questions using **custom documents and domain-specific information** without retraining the language model.

---

## 🌐 Deployment

The Gradio application is deployed on **Hugging Face Spaces**.

### Live Application

https://huggingface.co/spaces/adnanphp/rag-chatbot-tinyllama

### Local API

```text
http://localhost:8000
```

---

## 🔮 Future Improvements

Potential improvements include:

* [ ] PDF document ingestion
* [ ] DOCX document ingestion
* [ ] Better document chunking
* [ ] Metadata filtering
* [ ] Conversation memory
* [ ] Retrieval evaluation
* [ ] Precision@K and Recall@K evaluation
* [ ] Cross-encoder reranking
* [ ] Streaming responses
* [ ] API authentication
* [ ] Docker deployment
* [ ] Kubernetes deployment
* [ ] MLflow experiment tracking
* [ ] Support for larger or quantized LLMs

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Adnan**

GitHub:
https://github.com/adnanphp

Hugging Face:
https://huggingface.co/adnanphp

---

## 🔗 Project Links

| Resource              | Link                                                         |
| --------------------- | ------------------------------------------------------------ |
| 🤗 Hugging Face Space | https://huggingface.co/spaces/adnanphp/rag-chatbot-tinyllama |
| 💻 GitHub Repository  | https://github.com/adnanphp/rag-chatbot-tinyllama            |

---

> **Portfolio Project:** An end-to-end LLM application demonstrating **RAG, semantic retrieval, vector search, TinyLlama, FastAPI, Gradio, and Hugging Face deployment**.
