import streamlit as st
import tensorflow as tf



model = tf.keras.models.load_model('palm_oil_grader_100.h5')

st.write("hi")
