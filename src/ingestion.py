import os
from llama_index.core import StorageContext, VectorStoreIndex, SimpleDirectoryReader
from config import configure_settings, get_vector_store

def run_ingestion(data_path: str):
    """Loads PDFs and indexes them into Qdrant."""
    configure_settings()
    
    vector_store = get_vector_store()
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    print(f"📂 Reading files from {data_path}...")
    documents = SimpleDirectoryReader(data_path).load_data()
    
    print("🧠 Creating embeddings and storing in Qdrant...")
    index = VectorStoreIndex.from_documents(
        documents, 
        storage_context=storage_context,
        show_progress=True
    )
    
    print("✅ Ingestion complete.")
    return index

if __name__ == "__main__":
    DATA_DIR = "./data"
    if os.path.exists(DATA_DIR) and os.listdir(DATA_DIR):
        run_ingestion(DATA_DIR)
    else:
        print(f"❌ Error: {DATA_DIR} is empty or missing.")