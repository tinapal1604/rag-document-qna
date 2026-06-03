import warnings
warnings.filterwarnings("ignore")

from langchain_community.document_loaders import PyPDFLoader

def pdf_loader(file_path: str):
    loader = PyPDFLoader(file_path=file_path)
    docs = [doc for doc in loader.lazy_load()]
    return docs
