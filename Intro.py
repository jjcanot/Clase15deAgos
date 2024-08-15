import streamlit as st
from PIL import Image

image = Image.open('Pintupro.png')

st.title("PINTUPRO")

st.header("Soluciones creativas a tu alcance")
st.write("Contactanos al 300 691 6726")


texto = st.text_input('Describe el espacio a intervenir', 'Este es mi texto')
st.write("El espacio es", texto)

st.subheader("Queremos conocer más sobre el espacio a intervenir")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Información sobre el espacio a intervenir")
    st.write("¿Tu espacio esta amueblado?")
    resp = st.checkbox('Sí')
    if resp:
       st.write('Perfecto, llevaremos con que cubrir tus muebles y el piso')
    resp = st.checkbox('No')
    if resp:
       st.write('Perfecto, llevaremos para cubrir tu piso')
        
with col2:
     st.subheader("Esta es la segunda columna")
     modo = st.radio("Que modalidad es la principal en tu interfaz", ('Visual','Auditiva','Táctil'))
     if modo == 'Visual':
         st. write('La vista es fundamental para tu interfaz')
     if modo == 'Auditiva':
         st. write('La audición es fundamental para tu interfaz')
     if modo == 'Táctil':
         st. write('El tacto es fundamental para tu interfaz')

with st.slidebar:
    st.subheader("Configurar la modalidad")
    
