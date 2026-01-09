import os
from llama_index.core import (
    StorageContext, 
    VectorStoreIndex, 
    SimpleDirectoryReader
)

from config import configure_settings, get_vector_store

def run_ingestion(data_path: str):
    """
    Main pipeline to load PDFs and index them into Qdrant.
    """
    # 1. Initialize our global settings (Ollama, Chunk size, etc.)
    configure_settings()
    print(f"📂 Loading documents from: {data_path}")

    vector_store = get_vector_store()
    
    # Storage Context is a container that tells LlamaIndex where to store the data
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # 3. Load the actual PDF files
    documents = SimpleDirectoryReader(data_path).load_data()
    
    # 4. Build the Index
    print("🧠 Transforming text into vectors and storing them in Qdrant...")
    index = VectorStoreIndex.from_documents(
        documents, 
        storage_context=storage_context,
        show_progress=True
    )
    
    print("✅ Ingestion complete! Your D&D manual is now indexed.")
    return index

if __name__ == "__main__":
    # Ensure the 'data' directory exists and contains your PDF
    DATA_DIR = "./data"
    
    if not os.path.exists(DATA_DIR) or not os.listdir(DATA_DIR):
        print(f"❌ Error: Please put your D&D PDF in the '{DATA_DIR}' folder.")
    else:
        run_ingestion(DATA_DIR)