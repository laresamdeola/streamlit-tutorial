import streamlit as st
import pandas as pd
import numpy as np
import math

df_one = pd.DataFrame({
    'first column': [1, 2, 3, 4, 5],
    'second column': ['A', 'B', 'C', 'D', 'E']
})

# df

name_of_table = 'Random Data'
# st.write(name_of_table)

df = pd.DataFrame({
    'age': [10, 20, 30],
    'names': ['Lare', 'Chika', 'Melody']
})

# st.write(df)

# Using the dataframe

# st.dataframe(df.style.highlight_max(axis=0))

# Using a static table

# st.table(df)

# Plots

# Line Plots

# st.line_chart(df)

chart_data = pd.DataFrame(
    ([10, 20, 30], [15, 25, 35], [12, 22, 32]), 
    columns=['a', 'b', 'c']
    )

# st.line_chart(chart_data)

# Maps

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

# st.map(map_data, size=0.05)

# Widgets

# st.write('Widgets')

# x = st.slider('x')
# st.write(x, 'squared is', math.pow(x, 2))

# Text Input

# st.write('Text Input')
# st.text_input('Your Age', key='age')
# st.session_state.age

# Checkboxes

# if st.checkbox('Show Dataframe'):
#     chart_data_2 = pd.DataFrame(
#         np.random.randn(20, 3),
#         columns=['a', 'b', 'c']
#     )

#     chart_data_2

# Selectbox

# option = st.selectbox(
#     'which number do you like best?',
#     df_one['first column']
# )

# 'You selected: ', option

# Sidebar

# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home', 'Mobile')
# )

# # Add a slider to the sidebar
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

# Other Layout options

# left_column, right_column = st.columns(2)
# left_column.button('Press me!')

# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ('Gryfindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin')
#     )
#     st.write(f'You are in {chosen} house!')

# Show Progress

import time

# 'Starting a long computation'

# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#     latest_iteration.text(f'Iteration {i+1}')
#     bar.progress(i+1)
#     time.sleep(0.1)

# '... and now we\'re done!'

# Caching

# @st.cache_data
# # good for serializable objects like strings, int, list, dataframes etc

# @st.cache_resource
#good for non-serializable objects or data that can't be stored in a database e.g 
# ml models, database connections etc.

# Session State

# Example

import re

# st.text_input('Enter your name', key='name', value='Jack Smith')

# if st.session_state.name.isalpha():
#     st.write(st.session_state.name)
# if re.findall( '[0-9]', st.session_state.name):
#     st.write('Name can not contain numbers')


# Connections

# Theming

# Pages

# st.write('This is the Main Page')
# # st.markdown('Main Page')
# st.sidebar.markdown('# Main Page')


#I'm here

# Static File Serving

# App Testing

# Fetching datasets online

DATE_COLUMN = 'date/time'
DATA_URL = ('https://www.kaggle.com/datasets/aspillai/netflix-stock-price-with-indicators?select=nflx_2014_2023.csv')

@st.cache_data
def load_data(n_rows):
    data = pd.read_csv('uber-raw-data-sep14.csv', nrows=n_rows)
    data.rename(columns={'Lat': 'lat', 'Lon': 'lon'}, inplace=True)
    return data
    # lowercase = lambda x: str(x).lower()
    # data.rename(lowercase, axis='columns', inplace=True)
    # data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])

dataset = load_data(10)

# st.dataframe(dataset)

# st.subheader('Raw data')
# st.write(dataset)

# st.subheader('Map of all pickups')
# st.map(dataset)

# hour_to_filter = 40.74
# print(dataset[dataset['lat'] < hour_to_filter])

st.subheader('Raw Data')

if st.checkbox('Show raw data'):
    st.subheader('Raw Data')
    st.write(dataset)