import streamlit as st
from tensorflow import keras
from keras.models import load_model
import numpy as np
import PIL
model1 = load_model('Banana_inception.h5')
model = load_model('Banana_Resnet.h5')
st.title("Banana fruit grader") 
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
if uploaded_file is not None: 
            image = keras.preprocessing.image.load_img(uploaded_file, target_size=(224, 224))
            st.image(image, caption='Uploaded Image.', use_column_width=True)
            image = keras.preprocessing.image.img_to_array(image)
            image = np.expand_dims(image, axis=0)
            class_names = ['Unripe', 'Fresh Ripe', 'Ripe', 'Overripe'] 
            prediction = model1.predict(image)             
            class_index = np.argmax(prediction[0])
            class_probs = {class_names[i]: round(float(prediction[0][i]), 2) for i in range(len(class_names))}
            
            with st.container():
                 st.write("Prediction Results by Inception V3")
                 for class_name, prob in class_probs.items():
                    st.write(f"{class_name}:")
                    st.progress(prob)
            st.write("Classification Result by Inception V3:",class_names[class_index])
            prediction = model.predict(image)             
            class_index1 = np.argmax(prediction[0])
            class_probs1 = {class_names[i]: round(float(prediction[0][i]), 2) for i in range(len(class_names))}
            with st.container():
                 st.write("Prediction Results by Resnet-50")
                 for class_name, prob in class_probs1.items():
                    st.write(f"{class_name}:")
                    st.progress(prob)
            st.write("Classification Result by Resnet-50:",class_names[class_index1])
