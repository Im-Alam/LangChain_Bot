import streamlit as st
from dotenv import load_dotenv
from typing import List
from PyPDF2 import PdfReader
import os

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_google_vertexai import VertexAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import huggingface_hub
from langchain_groq import ChatGroq
from langchain_google_vertexai import VertexAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from htmlTemplate import css, bot_template, user_template



def extract_text_from_pfd(pdf_docs)->str:
    text_ = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text_ += page.extract_text()
    # print(text_)
    return text_

def chunk_text(txt: str)->List[str]:
    text_splitte = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 100,
        separators= ["\n\n", "\n", ".", " ", ""]
    )
    chunks = text_splitte.split_text(txt)
    # print(chunks)
    # st.write(chunks[0:4])
    return chunks

def embed_text(text_chunk):
    embeddings = VertexAIEmbeddings(model_name="text-embedding-004") #  using VertexAIEmbeddings with free $300 credits
    # embeddings = OpenAIEmbeddings() # shows: quota excedded
    vector_store = FAISS.from_texts(texts=text_chunk, embedding = embeddings)
    print(vector_store)
    return vector_store



def get_conversation_chain(vector_store):
    llm = ChatGroq(temperature=0.5, model_name="mixtral-8x7b-32768")
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory
    )

    return conversation_chain


def handle_user_input(user_question):
    response = st.session_state.conversation({"question":user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i%2 == 0:
            st.write(user_template.replace("{{msg}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{msg}}", message.content),  unsafe_allow_html=True)


def main():
    load_dotenv()

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None 
    
    
    st.set_page_config(page_title="Chat with pdf", page_icon="books")

    st.markdown(css, unsafe_allow_html=True)
    st.header("📖 Chat with your PDF: Books")

    user_question = st.text_input("Ask question about document here...",)
    
    if user_question:
        if st.session_state.conversation is not None:
            handle_user_input(user_question)
        else:
            st.write("No context!!!  Pls upload your PDFs and click on Process")
    

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Uload your PDFs here and click on Process", accept_multiple_files=True, type=['pdf'])
        
        
        if st.button("Process"):
            if pdf_docs:
                with st.spinner("Processing"):
                    # Get text from PDF
                    raw_text = extract_text_from_pfd(st.session_state.pdf_docs)

                    # Chunk the texts gathered
                    text_chunks = chunk_text(raw_text)

                    # Create vector store
                    vector_store = embed_text(text_chunks)

                    # Setup conversation
                    st.session_state.conversation = get_conversation_chain(vector_store)
            else:
                st.write("Please upload atleast one PDF file.")









if __name__ == "__main__":
    main()
    

