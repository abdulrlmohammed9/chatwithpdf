# ChatWithPDF — Generative AI PDF Question Answering

A Python/Gradio application that answers natural-language questions about uploaded, text-based PDFs using retrieval-augmented generation (RAG). This repository includes an updated, simplified implementation (`app.py`) and the original coursework implementation (`original/chatwithpdf_legacy.py`).

## Architecture

`PDF upload → PyPDF2 text extraction → overlapping chunks → OpenAI embeddings → per-session in-memory cosine similarity retrieval (top 3) → OpenAI chat model → answer`

**Technologies:** Python, Gradio, PyPDF2, OpenAI API, NumPy. The legacy implementation used LangChain and FAISS; the updated implementation uses in-memory NumPy retrieval to reduce dependencies. Do not describe the updated app as using FAISS or LangChain.

## Setup

1. Install Python 3.10+ and create a virtual environment.
2. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your own OpenAI API key. Never commit `.env`.
4. Run:
   ```bash
   python app.py
   ```
5. Open the local Gradio URL, upload a text-based PDF, select **Process PDF**, and ask a question.

API usage may incur charges. Use non-sensitive documents that you are permitted to send to an external API.

## Code layout

- `app.py` — simplified, independently runnable Gradio application
- `original/chatwithpdf_legacy.py` — original uploaded LangChain/FAISS prototype, preserved for provenance; it may need older compatible dependencies and is not the default entry point
- `requirements.txt` — dependencies for `app.py`
- `.env.example` — API key template, not a real key
- `.gitignore` — excludes secrets, local development files, PDFs and generated indexes

## Current limitations

- Supports selectable-text PDFs; scanned PDFs without a text layer need OCR.
- No measured answer-quality or retrieval benchmark is included.
- Simple character chunking may split passages mid-sentence.
- Chunk references are not page-level citations.
- Very long PDFs may exceed embedding-request input limits.
- The updated implementation uses in-memory vectors, not a persistent vector database; indexed document state lasts only within the user session.
- No deployment, automated test suite, or production security guarantees are claimed.

## Provenance

The original uploaded `chatwithpdf.py` used Gradio, PyPDF2, LangChain, FAISS, and OpenAI for PDF Q&A. This repository provides a streamlined variant for easier publication. Test on your own permitted PDF before describing it as working end-to-end.

## Portfolio description

**ChatWithPDF — Retrieval-Augmented PDF Question Answering**: Developed a Python Gradio application for document-grounded question answering, including PDF text extraction, chunking, OpenAI embeddings, similarity-based retrieval, and LLM answer generation.
