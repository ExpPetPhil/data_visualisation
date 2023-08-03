import streamlit as st

import numpy as np

import pandas as pd

import os

st.write('Hello World')

file_name_list =[]
for i in os.listdir():
  if i.endswith('csv'):
    file_name_list.append(i)

st.write(file_name_list)

df = pd.read_csv('Bastar Craton.csv')
st.dataframe(df)

el_list= df.columns.tolist()[27:80]
x_axis = st.selectbox('select elements', el_list)

st.multiselect('select location', file_name_list, file_name_list[0])





