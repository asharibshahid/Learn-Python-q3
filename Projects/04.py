# Unit Converter
import streamlit as st
st.markdown("""
    <style>
            *{
                        background-color: #987; /* Black Background */
            color: white; /* White Text for better contrast */

            }
        body {
            
              

        }
        .weather-container {
            text-align: center;
            background: #fff;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)
def length_converter(value, from_unit, to_unit):
    conversions = {
        "meters": 1,
        "kilometers": 0.001,
        "miles": 0.000621371,
        "feet": 3.28084,
        "inches": 39.3701
    }
    return value * (conversions[to_unit] / conversions[from_unit])

def weight_converter(value, from_unit, to_unit):
    conversions = {
        "kilograms": 1,
        "grams": 1000,
        "pounds": 2.20462,
        "ounces": 35.274
    }
    return value * (conversions[to_unit] / conversions[from_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    
# Streamlit UI
st.title("Modern Unit Converter")
st.markdown("A simple and modern unit converter built with Streamlit.")

# Sidebar for category selection
category = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

# Input fields
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

if category == "Length":
    from_unit = st.selectbox("From", ["meters", "kilometers", "miles", "feet", "inches"])
    to_unit = st.selectbox("To", ["meters", "kilometers", "miles", "feet", "inches"])
    result = length_converter(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Weight":
    from_unit = st.selectbox("From", ["kilograms", "grams", "pounds", "ounces"])
    to_unit = st.selectbox("To", ["kilograms", "grams", "pounds", "ounces"])
    result = weight_converter(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    result = temperature_converter(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

st.markdown("---")
st.info("Developed with ❤️ using Streamlit")
