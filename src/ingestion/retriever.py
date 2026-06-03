from langchain_chroma import Chroma
from embedder import embedding_model


def retriever(query: str, k:int=3):
    vector_store = Chroma(
    collection_name="rag-docs", 
    embedding_function=embedding_model, 
    persist_directory="./chroma_db"
    )
    results = vector_store.similarity_search(query=query, k=k)
    return results