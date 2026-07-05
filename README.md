#  RAG Chatbot with TinyLlama

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)](https://fastapi.tiangolo.com)
[![Gradio](https://img.shields.io/badge/Gradio-Latest-orange)](https://gradio.app)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A lightweight **Retrieval-Augmented Generation (RAG)** chatbot that answers questions from your own documents using **TinyLlama**, **LangChain**, **FAISS**, **FastAPI**, and **Gradio**.

---

##  Overview

This project demonstrates how to build a complete RAG (Retrieval-Augmented Generation) system.

Instead of relying only on a language model's knowledge, the chatbot first searches your uploaded documents, retrieves the most relevant information, and then uses TinyLlama to generate an accurate answer.

This makes responses more reliable and grounded in your own data.

---

##  Features

-  Upload and index text documents
-  Semantic document retrieval using FAISS
-  Answer questions with TinyLlama
-  FastAPI REST API
-  Interactive Gradio web interface
-  Extensible document knowledge base
- Pure Python implementation

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| TinyLlama | Large Language Model |
| LangChain | RAG Pipeline |
| FAISS | Vector Database |
| Sentence Transformers | Text Embeddings |
| FastAPI | REST API |
| Gradio | Web Interface |
| Python | Backend |

---

##  Project Structure

```text
rag-chatbot-tinyllama/
│
├── app_rag.py             # FastAPI application
├── space_app.py           # Gradio interface
├── rag_optimized.py       # RAG pipeline
├── requirements.txt
├── README.md
│
├── documents/
│   └── sample.txt
│
├── models/
│
└── vector_store/
```

---

##  Installation

Clone the repository.

```bash
git clone https://github.com/adnanphp/rag-chatbot-tinyllama.git

cd rag-chatbot-tinyllama
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Running the FastAPI Server

```bash
python app_rag.py
```

Open:

```
http://localhost:8000
```

Interactive API documentation:

```
http://localhost:8000/docs
```

---

##  Running the Gradio Interface

```bash
python space_app.py
```

Open:

```
http://localhost:7860
```

---

##  Sample Knowledge Base

Create the `documents` folder if it does not exist.

```bash
mkdir -p documents
```

Create a sample document.

```text
Artificial Intelligence is the simulation of human intelligence processes by machines.

Machine Learning enables systems to learn from data without explicit programming.

Deep Learning uses neural networks with multiple layers for pattern recognition.

Natural Language Processing helps computers understand human language.

Computer Vision allows machines to interpret visual information.

Reinforcement Learning trains agents through rewards and punishments.

Transfer Learning applies knowledge from one task to another.
```

---

##  API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Root endpoint |
| GET | `/health` | Health check |
| POST | `/ask` | Ask a question |
| POST | `/add_document` | Add a document |
| GET | `/documents` | List indexed documents |

---

## Example API Request

```bash
curl -X POST http://localhost:8000/ask \
-H "Content-Type: application/json" \
-d '{
  "question":"What is Machine Learning?"
}'
```

---

## Example Response

```json
{
  "answer": "Machine Learning enables systems to learn from data without explicit programming."
}
```

---

##  Deployment

### GitHub

```bash
git add .
git commit -m "feat: complete RAG Chatbot with TinyLlama"
git push origin main
```

Repository:

```
https://github.com/adnanphp/rag-chatbot-tinyllama
```

---

### Hugging Face Spaces

Create a new **Gradio Space**.

Then push your repository.

```bash
git remote add space https://huggingface.co/spaces/adnanphp/rag-chatbot-tinyllama

git push space main
```

---

##  Verification

Run the FastAPI server.

```bash
python app_rag.py
```

Test the root endpoint.

```bash
curl http://localhost:8000/
```

Open Swagger UI.

```
http://localhost:8000/docs
```

Run the Gradio application.

```bash
python space_app.py
```

---

##  Future Improvements

- PDF document support
- DOCX document support
- Multiple LLM backends
- Chat history
- Streaming responses
- User authentication
- Docker deployment
- Cloud deployment
- Hybrid search
- Persistent vector database

---

## 📜 License

This project is licensed under the MIT License.

---

##  Author

**Adnan**

GitHub:

```
https://github.com/adnanphp
```

---

## ⭐ If you found this project useful

Please consider giving the repository a **star** on GitHub.
