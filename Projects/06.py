import streamlit as st

# Set Page Config
st.set_page_config(page_title="User Info Form", layout="centered")

# Custom Gradient Background
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
        }
        .stTextInput > label, .stNumberInput > label {
            font-size: 18px;
            font-weight: bold;
            color: white;
        }
        .stButton > button {
            background: linear-gradient(45deg, #ff758c, #ff7eb3);
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 8px;
            border: none;
            transition: 0.3s;
        }
        .stButton > button:hover {
            background: linear-gradient(45deg, #ff7eb3, #ff758c);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("✨ Beautiful User Info Form ✨")

# User Input Fields
name = st.text_input("Enter Your Name:" , placeholder=" Enter your name ")
age = st.number_input("Enter Your Age:", min_value=1, step=1  , placeholder=" Enter your age ") 
classs = st.text_input("Enter Your Class: "  , placeholder=" Enter your Class ")

# Submit Button
if st.button("Submit"):
    st.success(f"Your Name is **{name}**, Your Age is **{age}**, Your Class is **{classs}**")
