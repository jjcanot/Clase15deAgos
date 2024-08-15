import streamlit as st
from PIL import Image

st.title("PINTUPRO")

st.header("Soluciones creativas a tu alcance")
st.write("Contactanos al 300 691 6726")
image = Image.open("Pintupro.png")





st.write("El texto escrito es", texto)

st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Esta es la primera columna")
    st.write("Las interfaces multimodales mejoran la experiencia de usuario")
    resp = st.checkbox('Estoy de acuerdo')
    if resp:
       st.write('Correcto!')
