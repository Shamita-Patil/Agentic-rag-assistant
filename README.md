# Agentic RAG Assistant using Google Gemini

## Overview

Agentic RAG Assistant is an AI-powered question-answering system that combines Retrieval-Augmented Generation (RAG) with real-time web search. The application uses Google Gemini, ChromaDB, Sentence Transformers, and LangChain Agents to answer questions from multiple document types while supplementing responses with current information from the web when required.

The agent dynamically decides whether to retrieve information from internal documents, perform a web search, or combine both sources to generate accurate and context-aware responses.

---

## Key Features

* Multi-Document Retrieval-Augmented Generation (RAG)
* Agentic AI using LangChain Agents
* Google Gemini Integration
* Semantic Search using Embeddings
* ChromaDB Vector Database
* Real-Time Web Search using Serper API
* Multi-Format Document Support

  * PDF
  * TXT
  * DOCX
  * XLSX
* Source-Aware Responses
* Modular and Scalable Architecture

---

## Technologies Used

* Python
* Google Gemini 2.5 Flash
* LangChain
* ChromaDB
* Sentence Transformers
* Serper Search API
* PyPDF
* Python-Docx
* OpenPyXL
* Python-Dotenv

---

## Architecture

```text
Documents
(PDF / TXT / DOCX / XLSX)
          │
          ▼
Document Processing
          │
          ▼
Chunking
          │
          ▼
Embeddings
(Sentence Transformers)
          │
          ▼
ChromaDB Vector Store
          │
          ▼
LangChain Agent
     ┌───────────────┐
     │               │
     ▼               ▼
Document Tool   Web Search Tool
 (ChromaDB)        (Serper)
     │               │
     └───────┬───────┘
             ▼
       Google Gemini
             ▼
      Final Response
```

---

## Project Structure

```text
agentic-rag-assistant/

├── agents/
│   └── research_agent.py
│
├── config/
│   └── config.py
│
├── tools/
│   ├── pdf_tool.py
│   └── web_tool.py
│
├── utils/
│   ├── document_processor.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vectordb.py
│   └── retriever.py
│
├── documents/
│   ├── Company_Policies.pdf
│   ├── Employee_Handbook.txt
│   ├── FAQ.txt
│   ├── Employee_Benefits.docx
│   └── Sales_Report.xlsx
│
├── agentic_rag.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Supported File Types

Place your documents inside the `documents` folder.

* PDF (.pdf)
* Text (.txt)
* Word (.docx)
* Excel (.xlsx)

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/agentic-rag-assistant.git

cd agentic-rag-assistant
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

SERPER_API_KEY=YOUR_SERPER_API_KEY
```

---

## Run the Application

```bash
python agentic_rag.py
```

---

## Sample Questions

```text
What is the refund policy?

What employee benefits are available?

How many vacation days do employees receive?

What does the warranty cover?

Summarize the employee handbook.

What was the revenue in March?

What are the latest AI trends?

Compare company refund policies with industry standards.
```

---

## Example Workflow

```text
User Question
      │
      ▼
LangChain Agent
      │
      ├── Document Search
      │
      ├── Web Search
      │
      └── Both
      ▼
Google Gemini
      ▼
Final Answer
```

---

## Skills Demonstrated

* Retrieval-Augmented Generation (RAG)
* Agentic AI Systems
* Vector Databases
* Semantic Search
* Embeddings
* LangChain Agents
* Tool Calling
* Prompt Engineering
* Google Gemini Integration
* Information Retrieval
* AI Application Development

---

## Future Enhancements

* Conversational Memory
* Streamlit User Interface
* Hybrid Search
* Multi-Agent Workflows
* Report Generation
* LangGraph Integration

---

## Author

## Author

Built to demonstrate end-to-end implementation of Agentic AI, Retrieval-Augmented Generation (RAG), semantic search, vector databases, and Google Gemini-powered intelligent document retrieval systems.
