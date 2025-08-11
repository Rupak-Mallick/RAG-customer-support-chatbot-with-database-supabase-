from langchain.chat_models import init_chat_model
import os

llm = init_chat_model(api_key=os.getenv("GROQ_API_KEY"), model="qwen/qwen3-32b", model_provider="groq")

def llm_node(state, **kwargs):
    query = state["query"]
    docs = state["docs"]
    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
    You are a helpful customer support bot.
    You reply only based on knowledge base and don't tell anything more.
    Your response must be succinct and only what you have in your knowledge base.
    Use the following context to answer the user's query.

    Context:
    {context}

    Query: {query}
    """
    response = llm.invoke(prompt)
    return {"query": query, "docs": docs, "response": response}
