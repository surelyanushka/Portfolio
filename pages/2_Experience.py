import streamlit as st
import PIL
from PIL import Image 

page_icon = Image.open("images/car.png")
st.set_page_config(
    page_title='Anushka Tawte',
    page_icon=page_icon,
    layout="wide", 
)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
local_css("style/style.css")
st.header("EXPERIENCE")

with st.container():
    st.markdown("### Researcher | [VIDA NYU](https://vida.engineering.nyu.edu)")
    st.write("*Nov 2024 to Present*")
    image_column, text_column = st.columns((1,5))
    with image_column:
        st.image(Image.open('images/vida.jpeg'))
    with text_column:
        st.markdown("""
        -  Developed a multi-scale visualization tool for cells using **cuML and CUDA**, cutting load times by 85%.
        - Optimized **semantic zooming** using GPU-based clustering, cutting rendering time by 65% on **1M+ single-cell embeddings.**
        - Implemented interactive clustering to highlight cancer cell similarities and allow detailed drill-down views.
        
        `Research` `Visualization` `cuML` `CUDA``GPU` `BioMed`
        """)

with st.container():
    st.subheader("AI Research Intern | [NRG](https://www.nrgmr.com/)")
    st.write("*July 2024 to August 2024*")
    st.markdown("""
    - Leveraged statistical analysis and data science techniques to extract actionable insights from market data, aiding in strategic decision-making.
    - Utilized data mining and machine learning algorithms to identify market trends and consumer behavior patterns, supporting predictive modeling for business forecasting.
    - Conducted competitive analysis using advanced data analysis tools to explore market offerings, pricing strategies, and sales models, optimizing product positioning.
    
    `Python` `Research` `AI/ML` `Market Research`
    """)

with st.container():
    st.subheader("Software App Developer | Technical Team SIESGST")
    st.write("*July 2020 to Dec 2022*")
    image_column, text_column = st.columns((1,5))
    with image_column:
        st.image(Image.open('images/tech1.png'))
    with text_column:
        st.markdown("""
        - Led the strategic migration of the application's backend from **Java to Kotlin**, significantly enhancing code maintainability and facilitating advanced data integration with SQLite structured database, boosting app efficiency. 
        - Implemented Jetpack Compose to revolutionize the app's UI/UX design, catalyzing a **300% increase** in user engagement. 
        - Led a team to build and revamp the website [SIESGST Portal](https://portal.siesgst.ac.in/), significantly increasing engagement from **500 to over 2,000 active users**.           
        - Integrated essential features such as an assignment tracker, attendance system, and event calendar.
         
        `Java` `Kotlin` `Data Engineering` `Data Science` `UI/UX Designing` `Git` `HTML/CSS` `Javascript` `Postman`
        """)

with st.container():
    st.markdown("### Information Visualization Teaching Assistant | [New York University](https://www.nyu.edu/)")
    st.write("*Spetember 2024 to Present*")
    st.markdown("""
    - Monitored labs for over 50 students in a graduate-level course, providing real-time debugging support and guidance on information visualization concepts.
    - Developed and set up weekly quiz questions to assess students' understanding of key course materials.
    - Graded and reviewed weekly assignments, delivering constructive feedback and upholding academic standards with the use of JavaScript, D3.js, and Tableau.
    
    `Javascript` `D3.js` `Tableau` `Data Transformations` 
    """)
with st.container():
    st.subheader("Codechef Chapter Lead | [Codechef Chapter](https://arena.siesgst.ac.in/contests)")
    st.write("*July 2020 to November 2022*")
    image_column, text_column = st.columns((1,5))
    with image_column:
        st.image(Image.open('images/codechef.jpg'))
    with text_column:
        st.markdown("""
        - Spearheaded the formulation of challenging questions and incorporating comprehensive test cases for monthly coding contests, leading to a 35% boost in attendance at chapter events and initiatives.
        - Directed the machine learning team for developing a personalised set of coding problems based on user strengths, which significantly enhanced active participation and contributed to the advancement of coding skills.
        
        `Competitive Coding` ` Android Development` `Java` `Python` `AI/ML/CV`
        """)

with st.container():
    st.subheader("Grader for Numerical Analysis | [New York University](https://cims.nyu.edu/dynamic/)")
    st.write("*September 2024 to Present*")
    st.markdown("""
        - Graded assignments for over 30 students in the Mathematics department, providing detailed feedback to support student learning and improve academic performance.
        
        `MATLAB` `Python` `Calculus` `Linear Algebra`
    """)
