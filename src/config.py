import os
from dotenv import load_dotenv
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings
from qdrant_client import QdrantClient
from llama_index.vector_stores.qdrant import QdrantVectorStore

from llama_index.core import set_global_handler

load_dotenv()

def configure_settings():
    """
    Global configuration for the RAG pipeline.
    This sets up the local LLM and Embedding models using Ollama.
    """
    
    # Define the LLM (Large Language Model)
    Settings.llm = Ollama(
        model=os.getenv("LLM_MODEL"),
        base_url=os.getenv("OLLAMA_BASE_URL"),
        request_timeout=120.0  # Local LLMs can be slow, we give it more time
    )

    # Define the Embedding model
    Settings.embed_model = OllamaEmbedding(
        model_name=os.getenv("EMBED_MODEL"),
        base_url=os.getenv("OLLAMA_BASE_URL")
    )

    Settings.chunk_size = 512
    Settings.chunk_overlap = 50

    set_global_handler("arize_phoenix")

def get_vector_store() -> QdrantVectorStore:
    """
    Utility function to initialize the Qdrant Vector Store.
    Good Practice: Centralized connection logic (DRY principle).
    """
    client = QdrantClient(url=os.getenv("QDRANT_URL"))
    
    return QdrantVectorStore(
        collection_name=os.getenv("COLLECTION_NAME"), 
        client=client
    )

if __name__ == "__main__":
    print("🔄 Starting configuration...")
    configure_settings()
    print(f"✅ LLM Configured: {Settings.llm.model}")
    print(f"✅ Embedding Configured: {Settings.embed_model.model_name}")
    print(f"✅ Chunk Size set to: {Settings.chunk_size}")
    print(f"✅ Chunk Overlap set to: {Settings.chunk_overlap}")