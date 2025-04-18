import streamlit as st
import requests
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from constant import *
from PIL import Image
import json
import base64

page_icon = Image.open("images/car.png")
st.set_page_config(
    page_title='Anushka Tawte',
    page_icon=page_icon,
    layout="wide",
)

st.markdown('<div style="display: none">uptime: active</div>', unsafe_allow_html=True)

linkedin_url = "https://www.linkedin.com/in/anushka-tawte/"
email_url = "mailto:at5849@nyu.edu"
github_url = "https://github.com/surelyanushka"

# -----------------  loading assets  ----------------- #

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def social_icons(width=24, height=24, **kwargs):
    icon_template = '''
    <a href="{url}" target="_blank" style="margin-right: 20px;">
        <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
    </a>
    '''

    icons_html = ""
    for name, url in kwargs.items():
        icon_src = {
            "linkedin": "https://img.icons8.com/ios/50/linkedin.png",
            "github": "https://img.icons8.com/ios/50/github--v1.png",
            "email": "https://img.icons8.com/ios/50/new-post--v1.png"
        }.get(name.lower())

        if icon_src:
            icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

    return icons_html

local_css("style/style.css")



# ----------------- info ----------------- #
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:black;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

with st.container():
    col1,col2,col3 = st.columns([6,2,1])

    full_name = info['Full_Name']
    with col1:
        gradient('F0EBE3','F6F5F2','C7B7A3',f"Hi, I'm {full_name}!", info["Intro"])
        st.write("")
        

        # st.write(info['About'])

    with col2:
        st.image("images/portfolio_pic.jpg", width=200 )
    with col3:
        st.markdown(
    f"""
    <div class="social-icons">
        {social_icons(30, 30, LinkedIn=linkedin_url, Email=email_url, GitHub=github_url)}
    </div>
    """,
    unsafe_allow_html=True
)

        
with st.container():
    st.write(info['About'])

st.markdown('######')

# ----------------- skillset ----------------- #
with st.container():
    st.subheader('⚒️ Technical Skills')
    st.write('*Take a peek at other tabs to see my full skillset.*')

# Create skill category tabs
    tabs = st.tabs(["💻 Languages & Platforms", "🧰 Tools & DB", "🧠 Frameworks", "📊 Algorithms", "📜 Certifications"])

    with tabs[0]:
        st.markdown("""
        <p style='font-size:16px;'>
        <b>Languages:</b> Python, SQL, R, C++, C, JavaScript, Java, Bash, HTML/CSS<br>
        <b>Platforms:</b> GCP, AWS (EC2, S3)
        </p>
        """, unsafe_allow_html=True)
    with tabs[1]:

        st.markdown("**PostgreSQL**, **MongoDB**, **MySQL**, **Linux/Unix**, **Windows**, **Git**")

    with tabs[2]:
 
        st.markdown("**Tableau**, **PyTorch**, **Dask**, **Spark**, **Scikit Learn**, **LLMs**, **RAGs**, **TensorFlow**, **OpenCV**")

    with tabs[3]:

        st.markdown("**Decision Trees**, **Random Forests**, **Neural Networks**, **KNN**, **KMeans**, **DBScan**, **Regression**, **ARIMA**")

    with tabs[4]:
        st.markdown("""
        <ul style="color: #7BB661; font-weight: 600; font-size: 16px;">
            <li><a href="https://coursera.org/share/7f51859bc93dfb034af3457e769e6e67" target="_blank" style="color: #7BB661;">Machine Learning – DeepLearning.ai (Coursera)</a></li>
            <li><a href="https://www.cloudskillsboost.google" target="_blank" style="color: #7BB661;">30 Days of Google Cloud</a></li>
            <li><a href="https://www.codecademy.com/learn/learn-python-3" target="_blank" style="color: #7BB661;">Learn Python 3</a></li>
        </ul>
        """, unsafe_allow_html=True)

