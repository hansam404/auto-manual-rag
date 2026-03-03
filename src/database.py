import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from src.ingest import load_and_chunk_pdf

DB_DIR = "./chroma_db"  

def get_embedding_model():
    """Uses a free, fast, local embedding model from Hugging Face."""
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def build_vector_db(pdf_path: str):
    """Processes PDF and stores embeddings in ChromaDB."""
    chunks = load_and_chunk_pdf(pdf_path)
    embeddings = get_embedding_model()
    
    print("Building Vector Database... This may take a moment.")
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_DIR
    )
    return vector_store

if __name__ == "__main__":
    build_vector_db("data/manual.pdf")
    print("Database built successfully at ./chroma_db")
