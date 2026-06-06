from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma  import Chroma

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def store_embeddings(chunks, persist_directory = "./chroma_db"):
    import chromadb
    client = chromadb.PersistentClient(path=persist_directory)
    try:
        client.delete_collection("rag-docs")
    except ValueError:
        pass

    vector_store = Chroma(
     collection_name="rag-docs",
     embedding_function=embedding_model,
     persist_directory=persist_directory
    )
    vector_store.add_documents(chunks)
    return vector_store


if __name__ == "__main__":
    import sys
    sys.path.append("src/ingestion")
    from loader import pdf_loader
    from chunker import chunk_docs

    pages = pdf_loader("C:\\MTech\\rag_doc_qna\\data\\Geostatistical Analysis.pdf")
    chunks = chunk_docs(pages)
    db = store_embeddings(chunks)
    print("stored successfully..")
    print(db.get()['ids'].__len__(), "chunks in vector store.")