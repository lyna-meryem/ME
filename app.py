import streamlit as st
import base64

st.set_page_config(
    page_title="Aviation BI",
    page_icon="✈️",
    layout="wide"
)

def set_bg(image):
    with open(image, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg("assets/avion_bg.jpg")

st.markdown("<h1 style='color:white;'>✈️ Aviation BI Portfolio</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:white;'>Streamlit · Data · Aviation</h3>", unsafe_allow_html=True)
