import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from src.database import get_embedding_model, DB_DIR

load_dotenv()

def get_rag_chain():
    
    embeddings = get_embedding_model()
    vector_store = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
    
    system_prompt = (
        "You are an expert automotive systems engineer. "
        "Use ONLY the following pieces of retrieved context to answer the question. "
        "If you do not know the answer based on the context, say 'I cannot find this information in the service manual.' "
        "Context: {context}"
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])
    
    qa_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, qa_chain)
    
    return rag_chain

def ask_manual(question: str) -> str:
    chain = get_rag_chain()
    response = chain.invoke({"input": question})
    return response["answer"]

if __name__ == "__main__":
    test_question = "What is the recommended tire pressure?"
    print(f"Q: {test_question}")
    print(f"A: {ask_manual(test_question)}")