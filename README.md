# 📝 Transformer Summarizer API

A lightweight **FastAPI microservice** for text summarization using **HuggingFace Transformers (T5 & BART)**.  
Packaged with **Docker** for easy deployment.

---

## 🚀 Features
- **Abstractive Summarization (T5)** → Generates new sentences capturing the essence.  
- **Extractive Summarization (BART)** → Picks most relevant sentences from input.  
- **REST Endpoints** → Easy integration with any app.  
- **Deployment Ready** → `requirements.txt` + `Dockerfile`.  

---

## 🛠️ Setup

Clone repo and install requirements:
### bash
git clone https://github.com/divyansh286/Transformer-Summarizer-API.git
cd Transformer-Summarizer-API
pip install -r requirements.txt

### Run API:
uvicorn api:app --reload --port 8000

### 📌 Example Usage
cURL (T5 Abstractive)
curl -X POST "http://127.0.0.1:8000/summarize-abstractive" \
-H "Content-Type: application/json" \
-d '{"text":"Your long paragraph here"}'

### cURL (BART Extractive)
curl -X POST "http://127.0.0.1:8000/summarize-extractive" \
-H "Content-Type: application/json" \
-d '{"text":"Your long paragraph here"}'

### 🐳 Run with Docker
docker build -t transformer-summarizer .
docker run -p 8000:8000 transformer-summarizer

### 📁 Files

summarizer/core.py – Summarization logic (T5 + BART).

api.py – FastAPI microservice exposing /summarize-abstractive and /summarize-extractive.

requirements.txt – Python dependencies.

Dockerfile – Deployment container.

### 🧑‍💻 Tech Stack

Transformers → HuggingFace (T5, BART)

Framework → FastAPI

Serving → Uvicorn

Deployment → Docker

## 👤 Author

- **Divyansh**
- **AI Engineer | Data Science & GenAI Enthusiast**

- **💻 GitHub:[ divyansh286](https://github.com/divyansh286)**

- **🌐 Skills: LLMs, Transformers, FastAPI, Django REST, Docker, API Engineering**


