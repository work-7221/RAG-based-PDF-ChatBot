# Local RAG PDF Assistant

<div align="center">

### Chat with your PDFs — Completely Offline

An AI-powered **Retrieval-Augmented Generation (RAG)** application that enables intelligent conversations with PDF documents using **local Large Language Models**.

No OpenAI API. No cloud inference. Your documents stay on your machine.

---

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?style=for-the-badge&logo=streamlit)
![Ollama](https://img.shields.io/badge/Ollama-LLM-black?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorDB-success?style=for-the-badge)
![Sentence Transformers](https://img.shields.io/badge/SentenceTransformers-Embeddings-orange?style=for-the-badge)
![Intel](https://img.shields.io/badge/Intel-IPEX--LLM-blue?style=for-the-badge)

</div>

---

# Overview

This project is a **fully local RAG (Retrieval-Augmented Generation) system** that allows users to upload PDF documents and ask natural language questions about their contents.

Instead of relying on cloud APIs, the entire pipeline runs **locally**, making the application private, efficient, and suitable for offline usage.

The application combines:

- PDF Processing
- Intelligent Text Chunking
- Semantic Embeddings
- Chroma Vector Database
- Local LLM (Ollama)
- Intel IPEX-LLM Optimized Runtime
- Interactive Streamlit Chat Interface

---
# Learning Outcomes

This project helped me gain practical experience with:

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Semantic Search
- Local Large Language Models
- Embedding Models
- Prompt Engineering
- Streamlit Application Development
- Intel AI Software Stack
- Modular AI System Design

---
# Features

- Upload one or multiple PDF documents
- Chat with uploaded PDFs
- Semantic similarity search
- Persistent Chroma Vector Database
- Fully Local Inference
- No external API required
- Conversation history
- Intel IPEX-LLM accelerated inference
- Modular project architecture

---

# System Architecture

```

                    PDF Documents
                          │
                          ▼
                 PDF Text Extraction
                          │
                          ▼
        RecursiveCharacterTextSplitter
                          │
                          ▼
       SentenceTransformer Embeddings
                          │
                          ▼
              Chroma Vector Database
                          │
               User Question
                          │
                          ▼
             Similarity Search (Top-K)
                          │
                          ▼
              Prompt Construction
                          │
                          ▼
        Ollama Runtime (Intel IPEX-LLM)
                          │
                          ▼
                  Generated Response

```

---

# Technology Stack

| Component | Technology |
|------------|------------|
| Programming Language | Python |
| Frontend | Streamlit |
| PDF Processing | PyPDF |
| Chunking | RecursiveCharacterTextSplitter |
| Embeddings | SentenceTransformers |
| Vector Database | ChromaDB |
| LLM | Ollama |
| Inference Runtime | Intel IPEX-LLM |
| Local Model | Llama 3.1 |

---

# RAG Pipeline

The application follows a Retrieval-Augmented Generation workflow:

### 1. PDF Loading

- Reads uploaded PDF documents
- Extracts raw textual content

---

### 2. Text Chunking

The extracted text is divided into overlapping chunks using

```

RecursiveCharacterTextSplitter

```

Current Parameters:

```

Chunk Size : 500
Chunk Overlap : 100

```

---

### 3. Embedding Generation

Each chunk is converted into dense vector embeddings using

```

sentence-transformers/all-MiniLM-L6-v2

```

These embeddings capture the semantic meaning of the text.

---

### 4. Vector Storage

Generated embeddings are stored in

```

ChromaDB

```

allowing efficient semantic retrieval.

---

### 5. Semantic Retrieval

When the user asks a question,

- The query is embedded
- Similar document chunks are retrieved from ChromaDB
- Relevant context is selected

---

### 6. Prompt Construction

The retrieved context, user query, and conversation history are combined into a structured prompt.

---

### 7. Local LLM Response

The prompt is sent to a local Llama model running through Ollama, generating a grounded response using the retrieved context.

---

# ⚡ Intel IPEX-LLM Optimized Runtime

<p align="center">
  <img src="https://cdn.brandfetch.io/idTGhLyv09/theme/dark/idbKj2C6Xy.svg?c=1bxid64Mup7aczewSAYMX&t=1676261443468" width="180"/>
</p>

One of the unique aspects of this project is the use of **Intel IPEX-LLM** as the runtime layer for local inference.

Instead of using the default Ollama runtime alone, the application utilizes **Intel IPEX-LLM** to better leverage Intel hardware for running local Large Language Models.

### Benefits

- Faster local inference
- Better utilization of Intel hardware
- Completely offline execution
- Improved response generation
- No cloud APIs required

This enables an efficient local AI workflow while maintaining complete data privacy.

---

# 📂 Project Structure

```

RAG-PDF-Assistant/

│

├── Functions/
│ ├── PDF_Loader.py
│ ├── chunker.py
│ ├── embedding_generation.py
│ ├── storing_function_VDB.py
│ ├── Querior_Processor.py
│ ├── prompt_builder.py
│ └── Ollama_LLM.py
│
├── Chat_History/
│
├── chroma_db/
│
├── app.py
│
├── requirements.txt
│
└── README.md

```

---

# Installation

Clone the repository

```bash
git clone https://github.com/work-7221/RAG-based-PDF-ChatBot.git

cd RAG-PDF-Assistant
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start Ollama

```bash
ollama serve
```

Run the application

```bash
streamlit run app.py
```

---

# Screenshots

- Landing Page
<img src = "screenshots\ss1.png">

- Chat Interface
<img src = "screenshots\ss2.png">

- Upload PDF
<img src = "screenshots\ss3.png">

- Generated Answers
<img src = "screenshots\ss4.png">

- Background Processes
<img src = "screenshots\ss5.png">

---


# Future Improvements

This project serves as the foundation for a more advanced production-style RAG system.

Improvements include:

- Semantic Chunking (implemented)
- Hybrid Search (BM25 + Dense Retrieval)
- Metadata Filtering
- Query Rewriting
- Multi-Query Retrieval
- Cross-Encoder Re-ranking
- Context Compression
- Source Citations
- Retrieval Evaluation
- Improved UI/UX

| Features | Status |
| -------- | -------- |
| Semantic Chunking |  ✅Implemented |
| Hybrid Search (BM25 + Dense Retrieval) |  ➡️next up |
|  Metadata Filtering |  ➡️next up |
|  Query Rewriting | ❗Planned  |
|  Multi-Query Retrieval |  ❗Planned |
|  Cross-Encoder Re-ranking |  ❗Planned |
|  Context Compression |   ❗Planned|
|  Source Citations |  ❗Planned |
|  Retrieval Evaluation |  ❗Planned |
|  Improved UI/UX |  ❗Planned |


---

# Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to open an issue or submit a pull request.

---

# License

This project is released under the Apache 2.0 License.

---

# Author

**Rohan Kumar Maharana** 


Building AI Systems • RAG • Agentic AI • Full Stack AI

⭐ If you found this project useful, consider giving it a star!