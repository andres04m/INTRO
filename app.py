import streamlit as st 
from PIL import Image

st.title("Mi primera app!!")

st.header("En este espacio comienzo a desarrollar mis apliaciones para interfaces multimodales")
st.write("Facilmente puedo realizar backend frontend.")
image = Image.open('imagen1.jpg')

st.image(image, caption= 'Interfaces multimodales')

texto=st.text_input('ecsribe algo','este es mi texto')
st.write('el texto escrito es:',texto)

st.subheader('ahora usamos 2 columnas')

col1,col2=st.colum(2)

with col1:
  st.subheader("esta es la primera columna")
  st.write("las interfaces multimodales mejoran la experiencia del usuario")
  resp=st.checkbox('estoy de acuerdo')
  if resp:
    st.write('correcto')


with col2:
  st.subheader("esta es la segunda columna")
  modo=st.radio("que modalidad es la principal en tu interfaz",('visual','auditiva','tactil'))
  if modo == 'visual'
  st.write('la vista es fundamnetal para tu interfaz')
  if modo == 'auditiva'
  st.write('la audicion es fundamnetal para tu interfaz')
  if modo == 'tactil'
  st.write('el tacto es fundamnetal para tu interfaz')


st.subheader("uso de botones")
if st.button('presione el boton'):
  st.write('gracias por presionar')
  else
  st.write('no has presionado aun')
  
