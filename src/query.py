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

        print("\n📚 SOURCES USED:")
        for i, node in enumerate(response.source_nodes, 1):
            # Retrieve the score (relevance) and the text content
            score = node.score
            text = node.node.get_content()
            # Retrieve metadata (like page number or file name if available)
            metadata = node.node.metadata
            
            print(f"\n--- Source {i} (Relevance: {score:.2f}) ---")
            print(f"File: {metadata.get('file_name', 'Unknown')}")
            print(f"Content: {text[:200]}...") 
            print("-" * 30)