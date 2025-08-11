import gradio as gr
from graph import app
from db.supabase_client import supabase
import uuid

def generate_customer_id():
    return str(uuid.uuid4())

customer_id = generate_customer_id()

# Insert customer if not exists
def ensure_customer_exists(customer_id):
    # Check if customer already exists
    existing = supabase.table("customers").select("*").eq("id", customer_id).execute()
    if not existing.data:
        supabase.table("customers").insert({
            "id": customer_id,
            "name": "Guest User",  # Default name
            "email": f"{customer_id}@guest.local"
        }).execute()

def chat_with_agent(user_message, chat_history):
    global customer_id

    ensure_customer_exists(customer_id)  # ✅ Ensure customer exists in DB

    response_text = ""
    for step in app.stream({"query": user_message, "customer_id": customer_id}, stream_mode="values"):
        if "response" in step:
            response_text = step["response"].content if hasattr(step["response"], "content") else step["response"]

    supabase.table("chat_history").insert({
        "customer_id": customer_id,
        "message": user_message,
        "response": response_text
    }).execute()

    chat_history.append((f"User: {user_message}", f"Assistant: {response_text}"))
    return chat_history, chat_history

with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Customer Support AI Bot")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Type your question...")
    clear = gr.Button("Clear")
    state = gr.State([])

    def clear_history():
        global customer_id
        customer_id = generate_customer_id()
        ensure_customer_exists(customer_id)  # New customer for new session
        return [], []

    msg.submit(chat_with_agent, [msg, state], [chatbot, state])
    clear.click(clear_history, None, [chatbot, state])

demo.launch()
