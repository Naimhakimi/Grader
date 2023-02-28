import streamlit as st
from PIL import Image
image1 = Image.open("palm oil fruit.jpg")
image2 = Image.open("banana fruit.jpg")
image3 = Image.open("pineapple fruit.jpg")
st.set_page_config(
    page_title="FruitIQ",

)

st.title("FruitIQ")

st.sidebar.success("Select a fruit Grader above.")
html_code = """
    <style>
        p{
            color: black;
            font-size: 16px;
            font-weight: bold;
            font-family: monofonto;
        }
        h1{
           color: black;
            font-size: 39px;
            font-weight: bold;
            font-family: monofonto;
        }
        
    </style>
    <p>This system contains three type of fruit ripeness grading which is Palm Oil Fruit Bunch Ripeness Grader , Banana Ripeness Grader ,Pineapple Ripeness Grader The system use a Convolutioon Neural Network(CNN) Inception V3 and Resnet-50 each will grade the fruit</p>
"""
st.markdown(html_code, unsafe_allow_html=True)

st.image(image1,caption='Palm Oil', width=200)
st.image(image2,caption='Banana Fruit', width=200)
st.image(image3,caption='Pineapple Fruit', width=200)