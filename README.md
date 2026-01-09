# 🎲 Natural20-RAG

An advanced assistant for Dungeons & Dragons based on **RAG (Retrieval-Augmented Generation)** architecture. The project allows querying the Player's Handbook in natural language, providing precise rule citations.

## 🛠️ Tech Stack
- **Orchestrator:** LlamaIndex (Core)
- **Local LLM:** Ollama (Llama 3.1)
- **Local Embedding:** Ollama (nomic-embed-text)
- **Vector Database:** Qdrant (via Docker)
- **Environment:** Python 3.12 (Conda)
- **Observability:** Arize Phoenix

## 🚀 Project Setup

### 1. Python Environment
We use Conda to manage dependencies in an isolated way:
```bash
conda create -n natural20-env python=3.12 -y
conda activate natural20-env
pip install -r requirements.txt
```