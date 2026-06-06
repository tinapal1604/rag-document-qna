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


def ask(question: str, chat_history: list = None):
    if chat_history is None:
        chat_history = []

    history_text = ""
    for msg in chat_history:
        role = msg["role"]
        content = msg["content"]
        history_text += f"{role}: {content}\n"
    chunks = retriever(question, k=3)
    context = "\n\n".join([c.page_content for c in chunks])
    pages = sorted(set([cnk.metadata['page'] for cnk in chunks]))

    prompt = f'''Previous conversations
    {history_text}
    Context from a document:
    {context}
    Answer this question using  the context and conversation above:
    {question}
    '''
    response = llm.invoke(prompt)
    
    return {
        "answer": response.content,
        "sources": sorted(set([c.metadata['page'] for c in chunks]))
    }

if __name__ == "__main__":
   history = []

   q1 = "what is spatial autocorrelation?"
   ans1 = ask(q1, history)
   history.append({"role":"user", "content":q1})
   history.append({"role": "assistant","content":ans1})
   print(ans1)

   q2 = "can you give an example of that?"
   ans2 = ask(q2, history)
   print(ans2)