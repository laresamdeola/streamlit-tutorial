import streamlit as st
import pandas as pd
import numpy as np
import math

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4, 5],
#     'second column': ['A', 'B', 'C', 'D', 'E']
# })

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
