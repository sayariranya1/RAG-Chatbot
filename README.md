# 🤖 RAG CV Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that answers questions about a CV using **LangChain**, **FAISS**, **HuggingFace embeddings**, **FastAPI**, **Streamlit**, and **LLaMA 3.1 via OpenRouter**.

The system processes a PDF CV, splits its content into smaller chunks, converts the chunks into vector embeddings, stores them in a FAISS vector database, retrieves the most relevant information for a user question, and generates an answer using an LLM.

---

## 🌟 Features

* **PDF Document Processing**: Loads the CV PDF using `PyPDFLoader` and splits its content into chunks using `RecursiveCharacterTextSplitter`.

* **Semantic Vector Search**: Converts document chunks into embeddings using `sentence-transformers/all-MiniLM-L6-v2` and stores them in a local **FAISS** vector database.

* **Persistent Vector Store**: Creates the FAISS index the first time the application runs and reuses the existing index for subsequent queries.

* **RAG Pipeline**: Retrieves the most relevant document chunks and provides them as context to the language model.

* **LLM Integration**: Uses `meta-llama/llama-3.1-8b-instruct` through the OpenRouter API to generate context-aware answers.

* **FastAPI Backend**: Provides a REST API with an `/ask` endpoint for querying the RAG pipeline.

* **Streamlit Frontend**: Provides an interactive web interface called **Ranya CV Assistant** for asking questions about the CV.

---

## 🔄 RAG Pipeline

```text
CV PDF
   ↓
PyPDFLoader
   ↓
Text Chunking
   ↓
HuggingFace Embeddings
   ↓
FAISS Vector Store
   ↓
Semantic Retrieval
   ↓
LLaMA 3.1 via OpenRouter
   ↓
Generated Answer
   ↓
FastAPI
   ↓
Streamlit
```

---

## 📁 Project Structure

```text
RAG-Chatbot/

├── backend/
│   ├── app.py                 # FastAPI server and API endpoints
│   ├── rag.py                 # Vector store creation and RAG pipeline
│   ├── data/                  # CV PDF storage
│   └── faiss_index/           # Persisted FAISS vector store
│
├── frontend/
│   └── streamlit_app.py       # Streamlit user interface
│
├── .env.example               # Environment variable template
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies

* **Python**
* **LangChain**
* **FAISS**
* **HuggingFace Sentence Transformers**
* **LLaMA 3.1 8B Instruct**
* **OpenRouter**
* **FastAPI**
* **Streamlit**
* **PyPDF**
* **Pydantic**

---

## 🛠️ Prerequisites & Installation

### 1. Clone the repository

```bash
git clone https://github.com/sayariranya1/RAG-Chatbot.git

cd RAG-Chatbot
```

### 2. Create and activate a virtual environment

#### Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy `.env.example` to `.env` and add your OpenRouter API key.

```bash
cp .env.example .env
```

Inside `.env`:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

---

## 🚀 How to Run the Application

### Step 1 — Start the Backend

From the project root directory:

```bash
uvicorn backend.app:app --reload --port 8000
```

The FastAPI backend will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

### Step 2 — Start the Frontend

Open a second terminal, activate the virtual environment, and run:

```bash
streamlit run frontend/streamlit_app.py
```

The Streamlit application will usually be available at:

```text
http://localhost:8501
```

---

## 🔌 API

### `GET /`

Checks whether the API is running.

Example response:

```json
{
  "message": "RAG CV Chatbot API is running"
}
```

### `POST /ask`

Sends a question to the RAG pipeline.

Request:

```json
{
  "question": "What are Ranya's AI skills?"
}
```

Response:

```json
{
  "answer": "..."
}
```

---

## 📌 How It Works

1. The CV PDF is loaded using `PyPDFLoader`.
2. The extracted text is split into chunks.
3. Each chunk is converted into a vector embedding using `all-MiniLM-L6-v2`.
4. The embeddings are stored in a local FAISS vector store.
5. For a user question, the system retrieves the three most relevant chunks.
6. The retrieved context is passed to the LLaMA 3.1 language model through OpenRouter.
7. The generated answer is returned through the FastAPI backend.
8. Streamlit displays the answer to the user.

