import sys
sys.path.append("src/ingestion")
sys.path.append("src/generation")

from retriever import retriever
from chain import ask
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy


from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_huggingface import HuggingFaceEmbeddings
from datasets import Dataset

from langchain_groq import ChatGroq
from ragas.llms import LangchainLLMWrapper
import os
from dotenv import load_dotenv
load_dotenv()

groq_llm = LangchainLLMWrapper(ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
))


def run_ragas_eval(dataset: list):
    hf_dataset = Dataset.from_list(dataset)

    hf_embeddings = LangchainEmbeddingsWrapper(
        HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
    )

    results = evaluate(
        dataset=hf_dataset,
        metrics=[faithfulness, answer_relevancy],
        llm=groq_llm,
        embeddings=hf_embeddings
    )
    return results

def build_eval_dataset(test_question: list):
    dataset = []
  
    for item in test_questions:
        question = item["question"]
        ground_truth = item["ground_truth"]


        chunks = retriever(question, k=3)
        result = ask(question, [])
        answer = result["answer"]

        contexts = [c.page_content for c in chunks]

        dataset.append({
            "question": question,
            "answer": answer,
            "contexts": contexts,
            "ground_truth": ground_truth
        })
        
    return dataset
if __name__ == "__main__":
  import os
  import json
base_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(base_dir, "test_question.json")

with open(json_path, "r") as f:
    test_questions = json.load(f)
    
dataset = build_eval_dataset(test_questions)
    
for item in dataset:
    print("Q:", item["question"])
    print("A:", item["answer"])
scores = run_ragas_eval(dataset)
print("\n === RAGAS SCORE ===")
print(scores)