from fastapi import FastAPI
from pydantic import BaseModel

try:
    from backend.rag import get_rag_chain
except ImportError:
    from rag import get_rag_chain


app = FastAPI(
    title="RAG CV Chatbot"
)


# Create RAG chain once
qa_chain = get_rag_chain()


class QuestionRequest(BaseModel):
    question: str



@app.get("/")
def home():
    return {
        "message": "RAG CV Chatbot API is running"
    }



@app.post("/ask")
def ask_question(request: QuestionRequest):

    response = qa_chain.invoke(
        {
            "query": request.question
        }
    )

    return {
        "answer": response["result"]
    }