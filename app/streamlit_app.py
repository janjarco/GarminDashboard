import streamlit as st
import pandas as pd
import plotly.express as px

# %% Data import
# --------------------
data = pd.read_csv('../data/activities/processed/Activities_Garmin.csv')
# data filter if Avg HR > 0
data = data[data['Avg HR'] > 0]
data['Avg Pace'] = pd.to_datetime(data['Avg Pace'])


data.dtypes

# %% Header
# --------------------
st.header("Garmin Data Dashboard: Jan Jarco activities")


# %% Scatter plot
# --------------------
# scatter plot with variables to choose from dataset
x = st.selectbox('X axis', data.columns)
y = st.selectbox('Y axis', data.columns)

st.plotly_chart(px.scatter(data, x=x, y=y, color="Activity Type"))