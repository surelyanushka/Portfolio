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
st.header("EXTRACURRICULARS")
# Wat was your solution sir?
with st.container():
    st.subheader("Hackathon Winner")
    image_column, text_column = st.columns((1,4))
    with image_column:
        st.image('images/gdg.jpeg')
        st.image('images/hackathon2.JPG')
    with text_column:
        st.markdown("""
            - **Winner, GDG NYC Hackathon** – Developed a fashion-tech project utilizing Gemini API Pro, outperforming 100+ participants across New York.  
            - **Winner @ DJASCII, University-Level Hackathon** – Engineered a method for rapid cervical fracture detection, enhancing diagnostic efficiency.  
            - **Winner, Techxter Inter-University Competition** – Secured first place among 50+ teams for a cybersecurity project.  
            - **Runner-Up, Hackathon** – Recognized for conducting an exceptional literature survey research in the field of Deep Learning and ML.  
            """)


# 
with st.container():
    st.subheader("Official Volunteer | [Geolife Youth Club](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1712724&HistoricalAwards=false)")
    st.write("*2020*")
    image_column, text_column = st.columns((1,4))
    with image_column:
        st.image('images/gyc.png')
    with text_column:
        st.markdown("""
            - Developed a comprehensive educational curriculum, focusing on essential subjects like mathematics, science, and languages, to aid the learning of underprivileged children in India.
            - Designed engaging social media posters using Canva and Adobe XD, contributing to the digital outreach in India and effectively enhancing awareness of the NGO’s mission to educate and support underprivileged children.
            """)


with st.container(): 
    st.subheader("Core Orgnaizer, TEDx ")
    st.write("*June - October 2022*")
    image_column, text_column = st.columns((2,4))
    with image_column:
        st.image('images/TEDx.jpg')
    with text_column:
        st.markdown("""
            - Spearheaded and coordinated a multifaceted team of over 40 members for the prestigious TEDx event
            - Leveraged LinkedIn for outreach and marketing, securing sponsorship and surpassing attendance expectations by 40\% through strategic planning and engagement with industry professionals.
            """)
with st.container(): 
    st.subheader("Co-Founder, TechConnect")
    image_column, text_column = st.columns((2,5))
    with image_column:
        st.image('images/tclogo.svg')
    with text_column:
        st.markdown("""
            - Established and led Tech Connect, a vibrant community focused on empowering women in technology, providing a supportive platform for networking, professional development, and advocacy within the tech industry
            - Organized impactful speaker sessions with industry leaders and coordinated bootcamps.
            """)
        
# Add more extra curriculars



