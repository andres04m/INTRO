import streamlit as st 
from PIL import Image

st.title("Mi primera app!!")

st.header("En este espacio comienzo a desarrollar mis apliaciones para interfaces multimodales")
st.write("Facilmente puedo realizar backend frontend.")
image = Image.open('imagen1.jpg')

st.image(image, caption= 'Interfaces multimodales')
