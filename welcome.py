import streamlit as st

import numpy as np

import pandas as pd

from bokeh.plotting import figure

import os

st.write('Hello World')

file_name_list =[]
for i in os.listdir():
  if i.endswith('csv'):
    file_name_list.append(i)

st.write(file_name_list)

#df = pd.read_csv('Bastar Craton.csv')
#st.dataframe(df)

#df1 = pd.read_csv(file_name_list)
select_file = st.selectbox('select', file_name_list)
df = pd.read_csv(select_file)

el_list= df.columns.tolist()[27:80]

x_axis = st.selectbox('select elements_x', el_list)
y_axis = st.selectbox('select elements_y', el_list)

#location = st.multiselect('select location', file_name_list, file_name_list[0])

#location = st.selectbox('select location', file_name_list)



#x = df['Mg']/10000
#y = df['Si']/10000
x = el_list
y = el_list

p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')

p.circle(x, y, legend_label='Trend', line_width=2)

p.line([0, 20],[5, 5])

st.bokeh_chart(p, use_container_width=True)






