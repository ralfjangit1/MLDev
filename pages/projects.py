import streamlit as st

st.set_page_config(page_title="Projects", layout="centered")

st.title("My Projects")

st.write("""
Here are some of my cool machine learning projects:

- ✅ **Student Performance Prediction**
- ✅ **Customer Churn Analysis**
- ✅ **Sleep Disorder Classifier**
- ✅ **Tuition Fee Propensity Predictor**
""")

if st.button("⬅ Back to Home"):
    st.switch_page("home.py")  # Only works in newer versions