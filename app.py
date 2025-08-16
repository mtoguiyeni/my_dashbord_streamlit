# app.py
import streamlit as st
import pandas as pd
from transform import clean_data as transform

df = pd.read_csv("data/data.csv")
df = transform(df)
st.line_chart(df.set_index("date")["value"])
