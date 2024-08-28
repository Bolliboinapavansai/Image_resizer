from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os
# import google.generativeai as genai
from PIL import Image
import io

# Configure Google Gemini Vision Model
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model = genai.GenerativeModel("gemini-1.5-flash")

# def get_response(question):
#     response = model.generate_content(question)
#     return response.text 

# Streamlit UI
st.set_page_config(page_title="Image Resizing")
st.header("Image Resizing")

# User input for prompt
#user_input = st.text_input("Input: ", key="input")

# Image upload
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png"])

# Desired image dimensions in inches
height_in_inches = st.number_input("Enter desired height (in inches)", min_value=1.0, format="%.2f")
width_in_inches = st.number_input("Enter desired width (in inches)", min_value=1.0, format="%.2f")
dpi = st.number_input("Enter DPI (Dots Per Inch)", min_value=1, value=300)

submit = st.button("Generate")

if submit:
    if uploaded_image:

        # Open the uploaded image using Pillow
        image = Image.open(uploaded_image)

        # Calculate pixel dimensions based on inches and DPI
        new_width = int(width_in_inches * dpi)
        new_height = int(height_in_inches * dpi)

        # Resize the image to the specified dimensions
        resized_image = image.resize((new_width, new_height), Image.LANCZOS)

        # Convert image to bytes
        img_byte_arr = io.BytesIO()
        resized_image.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        # Display the resized image
        st.image(resized_image, caption=f'Resized Image ({new_width}x{new_height})')

        # Provide a download link for the resized image
        st.download_button(
            label="Download Image",
            data=img_byte_arr,
            file_name="resized_image.jpg",
            mime="image/jpeg"
        )
    else:
        st.write("Please provide both a prompt and an image.")
