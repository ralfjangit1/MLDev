import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="My Portfolio", layout="centered")

st.title("My Portfolio")

html_code = """
<style>
    .card {
        background-color: #f4f4f4;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        max-width: 600px;
        margin: auto;
        font-family: Arial, sans-serif;
    }
    .profile-pic {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        object-fit: cover;
        margin-bottom: 10px;
    }
    .name {
        font-size: 26px;
        font-weight: bold;
        color: #333;
    }
    .bio {
        color: #555;
        margin-top: 5px;
        font-size: 16px;
    }
    .skills {
        margin-top: 15px;
    }
    .skills span {
        background-color: #e0e0e0;
        color: #333;
        padding: 5px 10px;
        border-radius: 20px;
        margin-right: 5px;
        font-size: 14px;
    }
    .links a {
        margin-right: 15px;
        text-decoration: none;
        color: teal;
        font-weight: bold;
    }
</style>

<div class="card">
    <center>
        <img src="https://avatars.githubusercontent.com/u/9919?s=200&v=4" class="profile-pic">
        <div class="name">Ralf Jangit</div>
        <div class="bio">Aspiring Data Scientist | Python & ML Enthusiast</div>
        <div class="skills">
            <span>Python</span>
            <span>Streamlit</span>
            <span>Machine Learning</span>
            <span>Data Analysis</span>
        </div>
        <div class="links" style="margin-top: 15px;">
            <a href="/projects" target="_self">🔗 View Projects</a>
        </div>
    </center>
</div>
"""

html(html_code, height=500)