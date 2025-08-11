from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List
from agents.retriever import retrieve_node
from agents.llm_node import llm_node
from agents.history_saver import save_history_node

class GraphState(TypedDict):
    query: str
    docs: List[str]
    response: str
    customer_id: int

graph = StateGraph(GraphState)
graph.add_node("retriever", retrieve_node)
graph.add_node("llm", llm_node)
graph.add_node("history", save_history_node)

graph.add_edge(START, "retriever")
graph.add_edge("retriever", "llm")
graph.add_edge("llm", "history")
graph.add_edge("history", END)

app = graph.compile()
