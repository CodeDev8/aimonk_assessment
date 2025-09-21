from os import environ

import requests
import streamlit as st
from PIL import Image

UI_BACKEND_HOST = environ.get("UI_BACKEND_HOST", "ui_backend")
UI_BACKEND_PORT = environ.get("UI_BACKEND_PORT", "8000")
OUTPUT_DIR = environ.get("OUTPUT_DIR", "outputs")

UI_BACKEND_URL = f"http://{UI_BACKEND_HOST}:{UI_BACKEND_PORT}/detect"

st.title("AI Monk Task Demo")
st.write("By Saran K")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    if st.button("Send to `ui_backend` service"):
        files = {"image": uploaded_file.getvalue()}
        try:
            response = requests.post(UI_BACKEND_URL, files=files)
            response.raise_for_status()
            response = response.json()
            detections = response.get("detections", [])
            st.write("Detections:")
            st.dataframe(detections)
            # for det in detections:
            #     st.write(f"- {det}")
            annotated_image_file_name = response.get("saved_files", [])
            for img_file_name in annotated_image_file_name:
                image = Image.open(OUTPUT_DIR + "/" + img_file_name)
                st.image(image, caption="Returned Image", use_container_width=True)
        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")
