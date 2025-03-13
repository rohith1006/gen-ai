import google.generativeai as genai
import streamlit as st

#apikey
genai.configure(api_key = "AIzaSyA0GzO1Yr0cIL7l0fIkNJk6NppXNtwMflo")

model = genai.GenerativeModel(model_name ="gemini-2.0-flash")

def get_response(input_question):
    response = model.generate_content(input_question)
    return response.text 

#streamlit
st.title("pssm gpt")
input = st.text_input("Enter your question ")
button = st.button("click me ")
if button:
    response = get_response(input)
    st.write(response)
