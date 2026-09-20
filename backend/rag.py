import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from langchain.chains import RetrievalQA


load_dotenv()


FAISS_PATH = "backend/faiss_index"
PDF_PATH = "backend/data/Ranya-Sayari-CV.pdf"


# -------------------------
# Create or load vectorstore
# -------------------------

def get_vectorstore():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


    # Load existing FAISS
    if os.path.exists(FAISS_PATH):

        print("Loading existing FAISS index...")

        vectorstore = FAISS.load_local(
            FAISS_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

        return vectorstore


    # Create FAISS for first time
    print("Creating new FAISS index...")


    loader = PyPDFLoader(PDF_PATH)

    documents = loader.load()

    print("Documents loaded:", len(documents))


    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )


    chunks = splitter.split_documents(documents)

    print("Chunks:", len(chunks))


    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )


    vectorstore.save_local(
        FAISS_PATH
    )


    print("FAISS saved successfully!")


    return vectorstore



# -------------------------
# RAG chain
# -------------------------

def get_rag_chain():

    vectorstore = get_vectorstore()


    llm = ChatOpenAI(
        model="meta-llama/llama-3.1-8b-instruct",
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1"
    )


    retriever = vectorstore.as_retriever(
        search_kwargs={
            "k": 3
        }
    )


    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )


    return qa_chain



# Test
if __name__ == "__main__":

    vectorstore = get_vectorstore()

    print("Vectorstore ready!")