import warnings
warnings.filterwarnings("ignore")
import os
from langchain_community.document_loaders import PyPDFLoader

def pdf_loader(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs


def load_folder(folder_path: str)-> list[str]:
    all_docs = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            path = os.path.join(folder_path, filename)
            docs = pdf_loader(path)
            all_docs.extend(docs)
    return all_docs
if __name__ == "__main__":
    folder = r"C:\MTech\rag_doc_qna\data"
    docs = load_folder(folder)
    print(len(docs), "pages loaded")
