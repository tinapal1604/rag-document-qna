# RAG Document QA

Ask questions about any PDF using natural language.

## Tech Stack
- LangChain + ChromaDB
- sentence-transformers (all-MiniLM-L6-v2)
- Llama 3.3 via Groq
- Python

## How it works
1. PDF is loaded, chunked and embedded locally
2. User question is matched against chunks via similarity search
3. Relevant chunks sent to Llama 3.3 for answer generation

## Setup
...