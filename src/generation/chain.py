import sys
import os
sys.path.append("src/ingestion")

import warnings
warnings.filterwarnings("ignore")

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from retriever import retriever

load_dotenv()


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)


def ask(question:str):
    chunks = retriever(question, k=3)
    context = "\n\n".join([c.page_content for c in chunks])
    prompt = f''' Here is some context from a document:
    {context}
    Answer this question using only the context above:
    {question}
    '''
    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":
    print(ask("what is spatial autocorrelation?"))