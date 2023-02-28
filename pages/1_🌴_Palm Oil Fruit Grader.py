import streamlit as st
from tensorflow import keras
from keras.models import load_model
import numpy as np
import PIL

model = load_model('palm_oil_grader_2023-02-19 01_45_59_150.h5')
model2 = load_model('palm_oil_grader Resnet_100.h5')
st.title("Palm oil Fruit Grader")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
if uploaded_file is not None: 
            image = keras.preprocessing.image.load_img(uploaded_file, target_size=(224, 224))
            st.image(image, caption='Uploaded Image.', use_column_width=True)
            image = keras.preprocessing.image.img_to_array(image)
            image = np.expand_dims(image, axis=0)
            class_names = ['Overripe', 'Ripe', 'Underipe', 'Unripe']  
            prediction = model.predict(image)          
            class_index = np.argmax(prediction[0])     
            class_probs = {class_names[i]: round(float(prediction[0][i]), 2) for i in range(len(class_names))}
            st.write("Prediction Results by Inception V3")
            for class_name, prob in class_probs.items():
                 st.write(f"{class_name}:")
                 st.progress(prob)
            st.write("Classification Result by Inception V3:",class_names[class_index])
            image1 = keras.preprocessing.image.load_img(uploaded_file, target_size=(331, 331))
            image1 = keras.preprocessing.image.img_to_array(image1)
            image1 = np.expand_dims(image1, axis=0)
            prediction = model2.predict(image1)          
            class_index1 = np.argmax(prediction[0])     
            class_probs1 = {class_names[i]: round(float(prediction[0][i]), 2) for i in range(len(class_names))}
            st.write("Prediction Results by Resnet-50")
            for class_name, prob in class_probs1.items():
                 st.write(f"{class_name}:")
                 st.progress(prob)
            st.write("Classification Result by Resnet-50:",class_names[class_index1])

            
