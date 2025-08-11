from db.supabase_client import supabase

def save_history_node(state):
    supabase.table("chat_history").insert({
        "customer_id": state.get("customer_id", 1),
        "message": state["query"],
        "response": str(state["response"])
    }).execute()
    return state
