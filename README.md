---

title: RAG Chatbot with TinyLlama
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: "6.19.0"
python_version: "3.10"
pinned: false
-------------

# 🤖 RAG Chatbot with TinyLlama

[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Space-yellow)](https://huggingface.co/spaces/adnanphp/rag-chatbot-tinyllama)
[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue)](https://github.com/adnanphp/rag-chatbot-tinyllama)
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)

> **A lightweight Retrieval-Augmented Generation (RAG) chatbot that combines semantic document retrieval with TinyLlama to answer questions from a custom knowledge base.**

[🚀 **Live Demo on Hugging Face Spaces**](https://huggingface.co/spaces/adnanphp/rag-chatbot-tinyllama)

---

## 📋 Overview

This project implements an end-to-end **Retrieval-Augmented Generation (RAG)** system using **TinyLlama** as the language model and **FAISS** for semantic retrieval.

Instead of relying only on the language model's pretrained knowledge, the chatbot first retrieves relevant information from a document collection and then provides that context to TinyLlama to generate an answer.

### 🔄 RAG Workflow

```text
                    ┌──────────────────┐
                    │     User Query   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Query Processing │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  FAISS Search    │
                    │ Semantic Retrieval│
                    └────────┬─────────┘
                             │
                       Relevant Context
                             │
                             ▼
                    ┌──────────────────┐
                    │    TinyLlama     │
                    │  Text Generation │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │     Answer       │
                    └──────────────────┘
```

---

## ✨ Features

| Feature                    | Description                                        |
| -------------------------- | -------------------------------------------------- |
| 📄 **Document Ingestion**  | Add documents to the chatbot's knowledge base      |
| 🔍 **Semantic Retrieval**  | Retrieve relevant information using vector search  |
| 🧠 **RAG Generation**      | Ground TinyLlama responses in retrieved context    |
| 🤖 **TinyLlama**           | Lightweight local language model for generation    |
| ⚡ **FAISS**                | Efficient vector similarity search                 |
| 🌐 **FastAPI**             | REST API for programmatic access                   |
| 🎨 **Gradio**              | Interactive web-based chatbot interface            |
| 🤗 **Hugging Face Spaces** | Public cloud deployment for the Gradio application |

---

## 🧠 RAG Architecture

The system follows a simple RAG pipeline:

```text
Documents
    │
    ▼
Document Ingestion
    │
    ▼
Text Processing / Embeddings
    │
    ▼
FAISS Vector Index
    │
    │
User Question
    │
    ▼
Semantic Search
    │
    ▼
Relevant Documents
    │
    ▼
Prompt + Retrieved Context
    │
    ▼
TinyLlama
    │
    ▼
Generated Answer
```

This architecture separates **information retrieval** from **language generation**, making it possible to update the knowledge base without retraining the language model.

---

## 🛠️ Tech Stack

| Technology              | Role                                |
| ----------------------- | ----------------------------------- |
| **Python**              | Application development             |
| **TinyLlama**           | Lightweight LLM for text generation |
| **FAISS**               | Vector similarity search            |
| **FastAPI**             | REST API                            |
| **Gradio**              | Interactive chatbot UI              |
| **Hugging Face Spaces** | Application deployment              |

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

Alternatively:

```bash
python space_app.py
```

The Gradio application will provide an interactive chatbot interface.

---

## 🌐 Deployment

The project is deployed using **Hugging Face Spaces** with Gradio.

### 🤗 Live Demo

https://huggingface.co/spaces/adnanphp/rag-chatbot-tinyllama

### 💻 Local API

```text
http://localhost:8000
```

---

## 📡 REST API

The FastAPI application provides the following endpoints:

| Method | Endpoint        | Description                           |
| ------ | --------------- | ------------------------------------- |
| `GET`  | `/`             | Root endpoint                         |
| `GET`  | `/health`       | API health check                      |
| `POST` | `/ask`          | Ask the RAG chatbot a question        |
| `POST` | `/add_document` | Add information to the knowledge base |
| `GET`  | `/documents`    | List available documents              |

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
├── space_app.py     # Gradio / Hugging Face application
│
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
└── LICENSE            # MIT License
```

---

## 🔑 Key Concepts Demonstrated

This project demonstrates practical experience with:

* **Retrieval-Augmented Generation (RAG)**
* **Large Language Models (LLMs)**
* **Semantic search**
* **Vector databases / vector indexing**
* **FAISS similarity search**
* **Prompt-based context injection**
* **FastAPI REST services**
* **Gradio interfaces**
* **LLM application deployment**
* **Hugging Face Spaces**

---

## 🎯 Why This Project?

Traditional LLM applications generate responses primarily from information encoded during model training.

A RAG system introduces an external knowledge source:

```text
Traditional LLM

Question ───────────────► LLM ───────────────► Answer


RAG

Question
   │
   ▼
Retriever ───► Relevant Context
                     │
                     ▼
                  TinyLlama
                     │
                     ▼
                   Answer
```

This approach allows the chatbot to work with **custom documents and domain-specific information** without fine-tuning the language model.

---

## 🔮 Future Improvements

Potential extensions include:

* [ ] Conversation memory
* [ ] PDF and DOCX document ingestion
* [ ] Document chunking and metadata filtering
* [ ] Retrieval evaluation with Precision@K and Recall@K
* [ ] Reranking with a cross-encoder
* [ ] Streaming LLM responses
* [ ] Authentication for the API
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

* GitHub: [@adnanphp](https://github.com/adnanphp)
* Hugging Face: [@adnanphp](https://huggingface.co/adnanphp)

---

## 🔗 Links

**GitHub Repository:**
https://github.com/adnanphp/rag-chatbot-tinyllama

**Live Hugging Face Space:**
https://huggingface.co/spaces/adnanphp/rag-chatbot-tinyllama

---

> 💡 **Portfolio Focus:** This project demonstrates an end-to-end LLM application combining **RAG, semantic retrieval, vector search, API development, and cloud deployment**.
