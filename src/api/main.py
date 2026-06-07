import sys
sys.path.append("src/generation")
from chain import ask

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str
    chat_history: list=[]

class AnswerResponse(BaseModel):
    answer: str
    sources: list
@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/ask")
def ask_question(request: QuestionRequest):
    result = ask(request.question, request.chat_history)
    return {
        "answer": result["answer"],
        "sources": result["sources"]
    }