import streamlit as st 
from PIL import Image

st.title("Mi primera app!!")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("Fácilmente puedo realizar backend frontend.")
image = Image.open('imagen1.jpg')

st.image(image, caption= 'Interfaces multimodales')

texto = st.text_input('escribe algo', 'este es mi texto')
st.write('el texto escrito es:', texto)

st.subheader('ahora usamos 2 columnas')

col1, col2 = st.columns(2)

with col1:
    st.subheader("esta es la primera columna")
    st.write("las interfaces multimodales mejoran la experiencia del usuario")
    resp = st.checkbox('estoy de acuerdo')
    if resp:
        st.write('correcto')

with col2:
    st.subheader("esta es la segunda columna")
    modo = st.radio("que modalidad es la principal en tu interfaz", ('visual', 'auditiva', 'táctil'))
    if modo == 'visual':
        st.write('la vista es fundamental para tu interfaz')
    elif modo == 'auditiva':
        st.write('la audición es fundamental para tu interfaz')
    elif modo == 'táctil':
        st.write('el tacto es fundamental para tu interfaz')

st.subheader("uso de botones")
if st.button('presione el botón'):
    st.write('gracias por presionar')
else:
    st.write('no has presionado aún')

