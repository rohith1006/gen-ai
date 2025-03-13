from PIL import Image
import streamlit as st

import google.generativeai as genai

genai.configure(api_key="AIzaSyDP_C8uKNv6BRCrMe7senBhftm6W8_AED8")

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

def get_response(image, prompt):
    response = model.generate_content([image, prompt])
    return response.text

# Streamlit

st.title("Lens")
image = st.file_uploader("Upload the image", type=["jpg", "png", "jpeg"])
input = st.text_input("Enter the question for image")
button = st.button("Click me")

# Display

if button:
    if image is not None:
        im = Image.open(image)
        st.image(im)
        output = get_response(im, input)
        st.write(output)
    else:
        st.write("Please upload an image.")