# imports
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

# code
# 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
# llama-3.3-70b-versatile
#prompt

prompt1=ChatPromptTemplate.from_messages([
    ("system","listen to the user's question"),
    ("user","give a detail answer based on question {question}") 
    ]) 
#LLM

llm = ChatGroq(
    model= "llama-3.2-11b-vision-preview",
    groq_api_key ="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",
    temperature= 0
    )
#output parser

op=StrOutputParser()

#chain
chain = prompt1|llm| op

#streamlit
st.title("Rohith GTP")
input_text = st.text_input("Enter your question or theme")
output = chain.invoke({"question":input_text})
st.write(output)