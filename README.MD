# RAG Document QA

Ask natural language questions over any PDF using open-source LLMs.

## Tech Stack
- LangChain + ChromaDB
- Llama 3.3 via Groq (free)
- sentence-transformers/all-MiniLM-L6-v2 (local embeddings)
- FastAPI + Streamlit
- Docker

## Evaluation (RAGAS)
| Metric | Score |
|--------|-------|
| Faithfulness | 0.66 |
| Answer Relevancy | 0.98 |

## How to run
1. Clone the repo
2. Add GROQ_API_KEY to .env
3. Run: docker-compose up

## Architecture
PDF → Chunking → Embedding → ChromaDB → Retrieval → Llama 3.3 → Answer