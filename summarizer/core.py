from transformers import pipeline

# Load HuggingFace pipelines
abstractive_summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")
extractive_summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_abstractive(text: str, max_length: int = 150, min_length: int = 40) -> str:
    """Summarize text using T5 (abstractive summarization)."""
    result = abstractive_summarizer(
        text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False
    )
    return result[0]["summary_text"]

def summarize_extractive(text: str, max_length: int = 150, min_length: int = 40) -> str:
    """Summarize text using BART (extractive summarization)."""
    result = extractive_summarizer(
        text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False
    )
    return result[0]["summary_text"]
