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
st.header("PROJECTS & PAPERS")

with st.container():
    st.subheader("NYC Car Crash Detection")
    st.write("*March 2024 - May 2024*")
    image_column, text_column = st.columns((2, 4))
    with image_column:
        # Insert image here
        st.image('images/nomo.png')
    with text_column:
        st.markdown("""
        - Leveraged Spark and Dask ML to manage and analyze extensive datasets of traffic, weather, and historical crash data, developing a Random Forest model that effectively predicted traffic accident hotspots with a 0.72 F1 score.
        - Created an interactive dashboard using Streamlit, which visualizes real-time data to aid in strategic decision-making.

        `Python` `Spark` `Dask ML` `Random Forest` `Streamlit`
        """)

with st.container():
    st.subheader("Fashion AId: Personal Outfit Recommender")
    st.write("*April 2024 - May 2024*")
    image_column, text_column = st.columns((2, 4))
    with image_column:
        # Insert image here
        st.image('images/FashionAId.png')
    with text_column:
        st.markdown("""
        - Engineered Fashion AId, utilizing Gemini 1.5 Pro and Stable Diffusion for advanced text-to-image generation, enhancing accessibility for visually impaired users by providing visual outfit suggestions.
        - Employed MongoDB to manage and store user wardrobe data for personalized recommendations.

        `Python` `Gemini 1.5 Pro` `Stable Diffusion` `MongoDB`
        """)

with st.container():
    st.subheader("Linux Disk I/O Optimization and Performance Enhancement")
    st.write("*November 2023 - December 2023*")

    st.markdown("""
    - Spearheaded a project focused on optimizing disk input/output performance in Linux, successfully enhancing file operation efficiency through strategic block size selection and multi-threading techniques.
    - Analyzed system call performance, identifying optimal block sizes to reduce overhead and increase I/O throughput.
    - Developed an algorithm processing 2.12 GB files in just 1 second in a Dockerized setup, demonstrating efficient multi-threading and block size optimization in a containerized environment.

    `Python` `Linux` `Docker` `Multi-threading`
    """)

with st.container():
    st.subheader("Spinescan AI")
    st.write("*July 2022 - April 2023*")
    image_column, text_column = st.columns((2, 4))
    with image_column:
        # Insert image here
        st.image('images/spine.png')
    with text_column:
        st.markdown("""
        - Enhanced diagnostic accuracy by developing a Convolutional Neural Network (CNN) using the EfficientNet architecture and Tensorflow, achieving a 95.2% classification accuracy rate for vertebral DICOM images.
        - Advanced fracture detection capabilities by integrating YOLOv5 object detection, attaining an 86% accuracy rate, demonstrating proficiency in deep learning and medical image analysis.

        `Python` `TensorFlow` `EfficientNet` `YOLOv5`
        """)

with st.container():
    st.subheader("Credit Card Fraud Risk Assessment")
    st.write("*March 2022*")

    st.markdown("""
    - Spearheaded a Credit Card Fraud Detection system, leveraging anomaly detection techniques to analyze transaction data and uncover fraud patterns, achieving a 93% accuracy with advanced machine learning algorithms.
    - Employed Jupyter Notebooks for model development and Matplotlib, Seaborn for insightful visualizations, significantly enhancing fraud identification processes and supporting a data-driven decision-making culture.

    `Python` `Jupyter Notebooks` `Matplotlib` `Seaborn`
    """)

with st.container():
    st.subheader("Malware Detection using Images")
    st.write("*July 2021 - February 2022*")
    image_column, text_column = st.columns((1, 5))
    with image_column:
        # Insert image here
        st.image('images/cc.png')
    with text_column:
        st.markdown("""
        - Developed a novel CNN (Convolutional Neural Network) to counter code obfuscation, leveraging binary representational images for malware identification, achieving a 92.7% accuracy rate.
        - Authored a published paper in IEEE Xplore, highlighting capabilities in security and research publication [link](https://ieeexplore.ieee.org/document/10142644).

        `Python` `TensorFlow` `Convolutional Neural Networks`
        """)

with st.container():
    st.subheader("Facial Recognition Attendance System")
    st.write("*February 2021 - December 2021*")
    st.markdown("""
    - Engineered a facial recognition attendance system using Python and OpenCV to ensure contactless attendance tracking during the pandemic, enhancing safety and operational efficiency.
    - Integrated a robust backend with MySQL for data management, facilitating real-time data capture and storage of attendance records, which supported efficient data retrieval and analysis for reporting purposes.

    `Python` `OpenCV` `MySQL`
    """)




