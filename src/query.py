import os
from llama_index.core import VectorStoreIndex

from config import configure_settings, get_vector_store

def create_query_engine():
    """
    Connects to the vector store and initializes the query engine.
    """
    configure_settings()

    vector_store = get_vector_store()

    # Define the index using the existing vector store
    index = VectorStoreIndex.from_vector_store(vector_store=vector_store)

    # Build the query engine
    return index.as_query_engine(similarity_top_k=3)

if __name__ == "__main__":
    query_engine = create_query_engine()
    
    print("\n--- 🎲 Natural20-RAG Query Interface ---")
    
    while True:
        query = input("\nAsk a rule question (or type 'exit'): ")
        
        if query.lower() in ["exit", "quit"]:
            break
            
        print("🔍 Searching the manual...")
        response = query_engine.query(query)
        
        print(f"\n📜 ANSWER:\n{response}")