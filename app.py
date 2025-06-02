import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Hello, Streamlit")
st.write("This is a test app running with Anaconda environment.")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Welcome, {name}!")


age = st.number_input("Enter your age:", min_value=1, max_value=100, value=25)
st.write(f"You are {age} years old.")

level = st.slider("Select your skill level:", 0, 10, 5)
st.write(f"Your skill level: {level}")

st.write("Here's a simple line chart:")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(chart_data)

st.write("Matplotlib example:")
fig, ax = plt.subplots()
ax.bar(['A', 'B', 'C'], [10, 20, 30])
st.pyplot(fig)
