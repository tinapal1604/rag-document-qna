from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_docs(docs:list):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunk = splitter.split_documents(docs)
    return chunk
