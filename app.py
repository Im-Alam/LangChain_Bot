import streamlit as st

from dotenv import load_dotenv
load_dotenv()



def main():
    st.set_page_config(page_title="Chat with pdf", page_icon="books")

    st.header("Chat with pdf: books")
    st.text_input("Ask question about document")

    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Uload your PDFs here and click on Process")
        st.button("Process")


if __name__ == "__main__":
    main()
