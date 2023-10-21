import streamlit as st
import pandas as pd
import plotly.express as px


data = pd.read_csv('../data/activities/processed/Activities_Garmin.csv')


st.header("Garmin Data Dashboard: Jan Jarco activities")

# scatter plot with variables to choose from dataset
x = st.selectbox('X axis', data.columns)
y = st.selectbox('Y axis', data.columns)

st.plotly_chart(px.scatter(data, x=x, y=y, color="Activity Type"))