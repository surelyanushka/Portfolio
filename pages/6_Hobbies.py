import streamlit as st
from PIL import Image
from constant import *
from io import BytesIO
import streamlit.components.v1 as components

page_icon = Image.open("images/car.png")
st.set_page_config(
    page_title='Anushka Tawte',
    page_icon=page_icon,
    layout="wide", 
)
st.header("HOBBIES")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style/style.css")



st.write("I’m a crafty STEM gal—dabbling in crochet, dance, photography, and anything that screams adventure. Master of many, bored of none.")
with st.container():
    col1,col2, col3, col4 = st.columns([2,2,2,2])
    with col1: 
      st.image("images/hobbies/art5.webp")
      st.image(("images/hobbies/dance2.jpg"))
      st.image("images/hobbies/crochet1.jpg")
      st.image("images/hobbies/sunset1.jpg")
    with col2: 
      st.image("images/hobbies/art3.png")
      st.image("images/hobbies/guitar2.jpg")
      st.image("images/hobbies/sunset2.jpg")
      st.image("images/hobbies/crochet2.jpg")
    with col3: 
      st.image("images/hobbies/raft.png")
      st.image("images/hobbies/art2.jpeg")
      st.image(("images/hobbies/dance3.jpg"))
      st.image(("images/hobbies/dance1.jpg"))
    with col4: 
      st.image(("images/hobbies/crochet3.jpg"))
      st.image("images/hobbies/3dprinting1.jpg")
      st.image(("images/hobbies/art1.jpeg"))
      st.image("images/hobbies/guitar1.jpg")


