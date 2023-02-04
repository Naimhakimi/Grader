import streamlit as st
from keras.models import load_model
import numpy as np



model = load_model('palm_oil_grader_100.h5')

st.title("Grader")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
