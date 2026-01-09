from llama_index.core import VectorStoreIndex
from config import configure_settings, get_vector_store

def create_query_engine():
    """Initializes the RAG query engine."""
    configure_settings()
    vector_store = get_vector_store()
    index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
    return index.as_query_engine(similarity_top_k=3)

def main():
    query_engine = create_query_engine()
    print("\n🎲 Natural20-RAG Interface Ready")
    
    while True:
        query = input("\nAsk (or 'exit'): ")
        if query.lower() in ["exit", "quit"]:
            break
            
        print("🔍 Searching...")
        response = query_engine.query(query)
        
        print(f"\n📜 ANSWER:\n{response}")
        print("\n📚 SOURCES:")
        for i, node in enumerate(response.source_nodes, 1):
            metadata = node.node.metadata
            print(f"[{i}] {metadata.get('file_name')} | Score: {node.score:.2f}")

if __name__ == "__main__":
    main()