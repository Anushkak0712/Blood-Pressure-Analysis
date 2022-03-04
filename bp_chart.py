from turtle import title
import pandas as pd
import streamlit as  st
import plotly.express as px
from PIL import Image
import altair as alt
st.set_page_config(page_title='blood pressure analysis')
st.header('Blood pressure analysis')
st.subheader('Readings of blood pressure')
csv_file='bp_readings - mummy(4).csv'
df=pd.read_csv(csv_file,index_col=0,parse_dates=True)
print(df)
st.line_chart(df)