# 🎲 Natural20-RAG

Natural20-RAG is an advanced intelligent assistant for **Dungeons & Dragons (5e)**. It uses a **RAG (Retrieval-Augmented Generation)** architecture to analyze the Player's Handbook (PHB) and answer complex rule-related questions, providing precise and contextualized citations.

The goal of the project is to move from theory to practice by implementing advanced data retrieval techniques in a fully local and private environment.

---

## 🛠️ Tech Stack

- **Orchestrator:** [LlamaIndex](https://www.llamaindex.ai/) (Core)
- **Local LLM:** [Ollama](https://ollama.com/) (Model: `llama3.1:8b`)
- **Local Embedding:** Ollama (Model: `nomic-embed-text`)
- **Vector Database:** [Qdrant](https://qdrant.tech/) (Running in Docker)
- **Observability & Tracing:** [Arize Phoenix](https://phoenix.arize.com/)
- **Environment Management:** Python 3.12 (Conda)

---

## 📁 Project Structure

```text
natural20-rag/
├── data/              # Manuals in PDF format (e.g., Player's Handbook)
├── docker/            # Configurations for containerized infrastructure
│   └── docker-compose.yml
├── src/               # Python source code
│   ├── ingestion.py   # Script to load data into the Vector DB
│   └── query.py       # Script to query the assistant
├── qdrant_storage/    # Persistent database data (auto-generated)
├── ollama_data/       # Locally stored AI models (auto-generated)
├── .env               # Environment variables (sensitive configurations)
├── .gitignore         # File to exclude heavy data from Git
├── requirements.txt   # Project dependencies
└── README.md          # Main documentation
```

---

## 🚀 Project Setup

### 1. Python Environment (Conda)
Create an isolated environment to avoid library conflicts and properly manage local dependencies:

```bash
# Create the environment with Python 3.12
conda create -n natural20-env python=3.12 -y

# Activate the environment
conda activate natural20-env

# Install dependencies from the requirements.txt file
pip install -r requirements.txt
```

### 2. Infrastructure (Docker)
Start the database services, LLM engine, and observability platform. Ensure Docker Desktop is running:

```bash
# Start the containers in the background
docker compose up -d
```

### 3. Model Downloads (Ollama)
Models must be downloaded locally within the Ollama container before first use:

```bash
# Download the language model (LLM) for reasoning
docker exec -it natural20_ollama ollama pull llama3.1

# Download the embedding model for document vectorization
docker exec -it natural20_ollama ollama pull nomic-embed-text
```

---

## 📊 Dashboard & Monitoring

Once the Docker infrastructure is running, you can access the web control interfaces:

| Service          | URL                          | Description                                      |
|------------------|------------------------------|--------------------------------------------------|
| Qdrant Dashboard | http://localhost:6333/dashboard | Graphical management of the vector database and collections. |
| Arize Phoenix    | http://localhost:6006        | Monitoring traces, latency, and RAG response quality. |

---

## 🛠️ Useful Commands

- Check container status: `docker compose ps`
- View real-time logs: `docker compose logs -f`
- Stop all services: `docker compose stop`
- Clean restart (without data loss): `docker compose down && docker compose up -d`