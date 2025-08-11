from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from .embeddings import embeddings
from dotenv import load_dotenv
import os
load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index_name = "customer-support-kb"

if index_name not in pc.list_indexes().names():
    pc.create_index(name=index_name, dimension=768)

index = pc.Index(index_name)
vector_store = PineconeVectorStore(embedding=embeddings, index=index)
