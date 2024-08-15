import streamlit as st
from PIL import Image

image = Image.open('Pintupro.png')
st.title("PINTUPRO")

st.header("Soluciones creativas a tu alcance")
st.write("Contactanos al 300 691 6726")

texto = st.text_input('Describe el espacio a intervenir', '...')
st.write("El espacio es", texto)

st.subheader("Queremos conocer más sobre el espacio a intervenir")

col1, col2 = st.columns(2)

with col1:
    #st.subheader("Información sobre el espacio a intervenir")
    st.write("¿Tu espacio esta amueblado?")
    resp = st.checkbox('Sí')
    if resp:
       st.write('Perfecto, llevaremos con que cubrir tus muebles y el piso')
    resp = st.checkbox('No')
    if resp:
       st.write('Perfecto, llevaremos para cubrir tu piso')
        
with col2:
    # st.subheader("Esta es la segunda columna")
     modo = st.radio("¡Cuantas habitaciones tiene?", ('Una','Dos','Tres', 'Más'))
     if modo == 'Una':
         st. write('La intervención prodía llevar medio un día')
     if modo == 'Dos':
         st. write('La intervención podría llevar un día ')
     if modo == 'Tres':
         st. write('La intervención podría llevar uno o dos días')
     if modo == 'Más':
         st. write('Dinos cuantas habitaciones para poder calcular el tiempo que llevara la intervención')
         texto = st.text_input('¿Cuantas habitaciones tiene?', 'Habitaciones')
         st.write("Las habitaciones son", texto, " ")

with st.sidebar:
     st.subheader("Configurar la modalidad")
     mod_radio = st.radio("escoge la modalidad de uso",('La ropa', 'esta dormido', 'ninguna'))
    
