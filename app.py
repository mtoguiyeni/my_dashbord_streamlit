# app.py
import streamlit as st
import pandas as pd
from transform import clean_data

df = pd.read_csv("data.csv")
df = clean_data(df)
st.line_chart(df.set_index("date")["value"])
