import os
from dotenv import load_dotenv
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings, set_global_handler
from qdrant_client import QdrantClient
from llama_index.vector_stores.qdrant import QdrantVectorStore

load_dotenv()

def configure_settings():
    """Global configuration for the RAG pipeline."""
    set_global_handler("arize_phoenix")

    # Define the LLM (Large Language Model)
    Settings.llm = Ollama(
        model=os.getenv("LLM_MODEL"),
        base_url=os.getenv("OLLAMA_BASE_URL"),
        request_timeout=120.0
    )

    # Define the Embedding model
    Settings.embed_model = OllamaEmbedding(
        model_name=os.getenv("EMBED_MODEL"),
        base_url=os.getenv("OLLAMA_BASE_URL")
    )

    Settings.chunk_size = 512
    Settings.chunk_overlap = 50

def get_vector_store() -> QdrantVectorStore:
    """Centralized Qdrant connection logic."""
    client = QdrantClient(url=os.getenv("QDRANT_URL"))
    return QdrantVectorStore(
        collection_name=os.getenv("COLLECTION_NAME"), 
        client=client
    )