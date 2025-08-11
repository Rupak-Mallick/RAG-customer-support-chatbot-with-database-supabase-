***Customer Support AI Bot with Database***(h1)<br/>
This project is a Customer Support AI Bot that leverages LangChain, LangGraph, Pinecone vector database, and Supabase to build an intelligent chatbot system. It uses a retrieval-augmented generation (RAG) approach to answer user queries based on a knowledge base stored in a database, and stores chat history for future reference.

**Features**:<br/>
Retrieval-augmented chatbot powered by LangChain and LangGraph.

Connects to Supabase to fetch knowledge base data and save chat history.

Uses Pinecone vector database for semantic search and retrieval.

Embeddings generated with HuggingFace sentence-transformers.

Modular multi-step workflow with LangGraph states: retrieval, generation, and history saving.

Interactive chat UI built with Gradio for easy testing and demo.

Supports streaming response generation.

**Tech Stack**:<br/>
LangChain, LangGraph — for AI agent orchestration and LLM integration

Groq API (qwen3-32b model) — large language model backend

Supabase — Postgres-based backend for knowledge base and chat history

Pinecone — vector similarity search for knowledge retrieval

HuggingFace embeddings — semantic vector generation

Gradio — frontend chat interface

Google Colab — development environment

**Installation:**<br/>
Clone the repository.

**Install dependencies**:<br/>

bash
Copy
Edit
pip install langchain langgraph langchain-community langchain-groq pinecone-client supabase langchain-huggingface sentence-transformers langchain_pinecone gradio
Set environment variables for API keys (recommended via environment or Colab userdata):

GROQ_API_KEY — Your Groq API key for the LLM

PINECONE_API_KEY — Your Pinecone API key

Configure Supabase credentials inside the script:

python
Copy
Edit
SUPABASE_URL = "<your_supabase_url>"
SUPABASE_KEY = "<your_supabase_key>"
Usage
Run the notebook or script in a Python environment (Google Colab recommended).

The chatbot UI will launch via Gradio.

Enter your queries, and the bot will answer based on the knowledge base.

Chat history is saved in Supabase for future analysis or audit.

You can extend or customize the knowledge base by updating the Supabase table.

**Project Structure Overview**:<br/>
Knowledge Base: Stored in Supabase, indexed with Pinecone for fast semantic retrieval.

Workflow Graph:

Retriever Node: fetches relevant documents.

LLM Node: generates answers based on retrieved context.

History Node: saves conversation to database.

Frontend: Gradio chatbot interface to interact with the AI agent.

**Notes**:<br/>
The project requires valid API keys for Groq and Pinecone.

Make sure your Supabase tables (knowledge_base and chat_history) are set up correctly.

The LLM prompt is designed to restrict answers strictly to knowledge base content.

**Contributing**:<br/>
Contributions are welcome! Feel free to open issues or submit pull requests to improve the bot, add features, or fix bugs.
