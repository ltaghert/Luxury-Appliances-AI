import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA

def get_answer(query):
    if not os.path.exists('./manuals') or not os.listdir('./manuals'):
        return {"result": "No manuals found. Please run the scraper first."}
    
    pdf_files = [f for f in os.listdir('./manuals') if f.endswith('.pdf')]
    all_pages = []
    for pdf in pdf_files:
        loader = PyPDFLoader(f"./manuals/{pdf}")
        all_pages.extend(loader.load_and_split())

    vectorstore = Chroma.from_documents(
        documents=all_pages, 
        embedding=OpenAIEmbeddings(),
    )

    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model="gpt-4o"),
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )
    return qa.invoke(query)
