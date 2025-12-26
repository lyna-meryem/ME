import streamlit as st
import pandas as pd

st.title("📊 Dashboard BI")

df = pd.read_csv("data/ventes.csv")

col1, col2, col3 = st.columns(3)
col1.metric("CA", "12,4 M€", "+8%")
col2.metric("Vols", "1 245")
col3.metric("Taux remplissage", "82%")

st.line_chart(df["ventes"])
