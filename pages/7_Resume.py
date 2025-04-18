import streamlit as st
import base64
from constant import *
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
st.header("📄RESUME")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")


with open("images/Resume.pdf", "rb") as f:
    pdf_data = f.read()

st.download_button(
    label="Download Resume",
    data=pdf_data,
    file_name="Anushka_Tawte_Resume.pdf",
    mime="application/pdf",
    key="resume_download"
)

st.markdown("---")

# ---------- Contact & Socials ----------
st.subheader("📬 Connect with Me")

# Use columns for a neat layout
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.markdown("[![Email](https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:at5849@nyu.edu)")

with col2:
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/surelyanushka)")

with col3:
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/anushkatawte)")
