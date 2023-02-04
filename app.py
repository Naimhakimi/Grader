import streamlit as st
from tensorflow import keras
from keras.models import load_model
import numpy as np
import PIL



model = load_model('palm_oil_grader_100.h5')

st.title("fruit Grader")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    
  
    image = keras.preprocessing.image.load_img(uploaded_file, target_size=(331, 331))
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    image = keras.preprocessing.image.img_to_array(image)
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)
    class_names = ['Overripe', 'Ripe', 'Underipe', 'Unripe']
    
    class_index = np.argmax(prediction[0])
    st.write("Classification Result:",class_names[class_index])