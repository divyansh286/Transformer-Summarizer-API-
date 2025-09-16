from fastapi import FastAPI
from pydantic import BaseModel
from summarizer.core import summarize_abstractive, summarize_extractive

app = FastAPI(title="Transformer Summarizer API", version="1.0")

class SummarizeRequest(BaseModel):
    text: str
    max_length: int = 150
    min_length: int = 40

@app.post("/summarize-abstractive")
def summarize_t5(req: SummarizeRequest):
    """Abstractive summarization using T5."""
    return {"summary": summarize_abstractive(req.text, req.max_length, req.min_length)}

@app.post("/summarize-extractive")
def summarize_bart(req: SummarizeRequest):
    """Extractive summarization using BART."""
    return {"summary": summarize_extractive(req.text, req.max_length, req.min_length)}

@app.get("/health")
def health():
    return {"status": "ok"}
