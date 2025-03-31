import streamlit as st
import PIL
from PIL import Image 

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

page_icon = Image.open("images/car.png")
st.set_page_config(
    page_title='Anushka Tawte',
    page_icon=page_icon,
    layout="wide", 
)
local_css("style/style.css")
st.header("EDUCATION")
with st.container():
    st.subheader(" New York University Tandon School of Engineering | GPA: 3.75/4.0")
    st.write("*Master of Science, Computer Science*, Expected May 2025")
    image_column, text_column = st.columns((1,5))
    with image_column:
        st.image(Image.open('images/nyu.png'))
    with text_column:
        st.markdown("""
    **Selected Coursework**: Machine Learning, Design and Analysis of Algorithms, Foundations of Data Science, Big Data, Human Computer Interaction, Internet Security and Privacy, Advanced Project in Computer Science
    """)



with st.container():
    st.subheader("University of Mumbai | GPA: 3.8/4.0")
    st.write("*Bachelor of Engineering in Computer Engineering*, July 2023")
    image_column, text_column = st.columns((1,5))
    with image_column:
        st.image(Image.open('images/uom2.png'))
    with text_column:
        st.markdown("""
        **Selected Coursework**: Data Structures, Analysis of Algorithms, Deep learning, Machine Learning, Data warehousing and Mining, Cryptography, Python, Java
        """)
