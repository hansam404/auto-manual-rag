import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_and_chunk_pdf(
    file_path: str, chunk_size: int = 1000, chunk_overlap: int = 200
):
    """Loads a PDF and splits it into smaller text chunks."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    return text_splitter.split_documents(documents)


if __name__ == "__main__":
    chunks = load_and_chunk_pdf("data/manual.pdf")
    print(f"Successfully created {len(chunks)} chunks.")
