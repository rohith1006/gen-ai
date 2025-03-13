from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_cohere import CohereEmbeddings
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
import streamlit as st


# webbase data 

webdata = WebBaseLoader("https://www.pssmovement.org/")
data = webdata.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000 , chunk_overlap=200)
chunks = splitter.split_documents(data)

# embeddings
embeddings = CohereEmbeddings(
    model = "embed-english-v3.0",#open cohere embeddings langchain  and copy the model name 
    cohere_api_key="ZQZYzlZTljXRpNi7R5PecXcUSyJINiLe0t4XKMp7" 
    )

# vector store
vector_store = FAISS.from_documents(
    embedding=embeddings,
    documents=chunks
    )

# Ret 

retriever = vector_store.as_retriever()

# prompt
prompt2 = ChatPromptTemplate.from_template(
    """
    you have to answer only within the context {context}
    and precisely according to user asked question {question}
    """
    ) 

# llm
llm = ChatGroq(
    model="llama-3.2-11b-vision-preview",
    groq_api_key="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",
    temperature=0
    )

# output parser
op = StrOutputParser()

# chain
chain = (
    {"context":retriever,"question":RunnablePassthrough()}|
    prompt2|llm|op
)

#streamlit

st.title("WEB RAG")
input = st.text_input("Enter your question for website")
button = st.button("click me ")
if button:
    output = chain.invoke(input)
    st.write(output)