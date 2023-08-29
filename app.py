from dotenv import load_dotenv
from PyPDF2 import PdfReader
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback


def main():
    load_dotenv()
    st.set_page_config(page_title="Ask Your PDF")
    st.header("Ask Your PDF")

    #UPLOAD FILE
    pdf = st.file_uploader("Upload Your PDF Here ",type='pdf')

    #EXTRACT THE TEXT
    if pdf is not None:
        pdf_reader=PdfReader(pdf)
        text =""
        for page in pdf_reader.pages:
            text +=page.extract_text()
        
        #Splitting into chunks
        text_splitter = CharacterTextSplitter(
            separator='\n',
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)
        
        #creating embeddings
        embeddings = OpenAIEmbeddings()
        Knowledge_base = FAISS.from_texts(chunks,embeddings)

        #show user input
        user_question=st.text_input("Ask Anything!!!")

        #similarity search
        if user_question:
            docs = Knowledge_base.similarity_search(user_question)
            
            llm=OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")
            response = chain.run(input_documents=docs, question=user_question)

            st.write(response)

if __name__ == "__main__":
    main()