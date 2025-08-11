from vector_store.pinecone_store import vector_store

retriever = vector_store.as_retriever(search_kwargs={"k": 3})

def retrieve_node(state):
    query = state["query"]
    docs = retriever.get_relevant_documents(query)
    return {"query": query, "docs": docs}
