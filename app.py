import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("👋 Hello Streamlit!")
st.subheader("This is a simple interactive app.")

# Input from user
name = st.text_input("What's your name?")

# Display output
if name:
    st.success(f"Hello, {name}! Welcome to Streamlit. 🎉")
    st.write("Would you like to continue using streamlit?")
