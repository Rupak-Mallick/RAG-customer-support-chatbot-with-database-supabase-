from db.supabase_client import supabase
from vector_store.pinecone_store import vector_store

# Fetch knowledge base
kb_data = supabase.table("knowledge_base").select("*").execute()
knowledge_base = kb_data.data

if not knowledge_base:
    print("No knowledge base data found in Supabase.")
else:
    # Add data to Pinecone
    vector_store.add_texts(
        texts=[doc["content"] for doc in knowledge_base],
        metadatas=[{"title": doc["title"], "id": doc["id"]} for doc in knowledge_base]
    )
    print(f"Embedded {len(knowledge_base)} documents into Pinecone.")
