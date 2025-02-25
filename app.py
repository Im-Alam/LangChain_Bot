import streamlit as st
from dotenv import load_dotenv
from typing import List

from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain_google_vertexai import VertexAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.llms import openai # Will use davinchi
from langchain.llms import HuggingFaceHub
from langchain_google_vertexai import VertexAIEmbeddings
from langchain.chains import ConversationalRetrievalChain


PROJECT_ID = "linen-arch-452005-e6"  # @param {type:"string"}
LOCATION = "us-central1"  # @param {type:"string"}

import vertexai

vertexai.init(project=PROJECT_ID, location=LOCATION)


def extract_text_from_pfd(pdf_docs)->str:
    text_ = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text_ += page.extract_text()
    # print(text_)
    return text_

def chunk_text(txt: str)->list[str]:
    text_splitte = CharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 100,
        separator= '\n'
    )
    chunks = text_splitte.split_text(txt)
    
    return chunks

def embed_text(text_chunk):
    embeddings = VertexAIEmbeddings(model_name="text-embedding-004")
    vector_store = FAISS.from_texts(texts=text_chunk, embedding = embeddings)
    # print(vector_store)
    return vector_store



def get_conversation_chain(vector_store):
    llm = openai()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory
    )
    return conversation_chain






def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with pdf", page_icon="books")

    st.header("📖 Chat with your PDF: Books")
    st.text_input("Ask question about document")

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Uload your PDFs here and click on Process", accept_multiple_files=True, type=['pdf'])
        
        if st.button("Process"):
            with st.spinner("Processing"):
                # get text from pdf
                raw_text = extract_text_from_pfd(pdf_docs)
                #print(raw_text)

                # chunk the texts gathered
                text_chunks = chunk_text(raw_text)
                #st.write(text_chunks)

                # create vector store
                vector_store = embed_text(text_chunks)











if __name__ == "__main__":
    main()
    

