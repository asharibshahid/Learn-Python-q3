import streamlit as st
import requests

# 🌈 Custom Styling for UI
st.markdown("""
    <style>
            *{
                        background-color: #000000; /* Black Background */
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

# 🌤 App Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌤 Weather Forecast App</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #555;'>Get Real-Time Weather Updates ☁️</h3>", unsafe_allow_html=True)

# 🏙 User Input (City Name)
city = st.text_input("🌍 Enter city name:", placeholder="e.g. Karachi, Lahore, New York")

# 🔍 Fetch Weather Data
if city:
    api_key = "8441d0cf99fd44cf903151834243107"  # Replace with actual API Key
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # 🌡 Extract Weather Details
        weather = data['current']['condition']['text']
        temp = data['current']['temp_c']
        humidity = data['current']['humidity']
        wind_speed = data['current']['wind_kph']
        icon_url = "https:" + data['current']['condition']['icon']  # Weather Icon
        
        # 🎨 Weather Display Card
        with st.container():
            st.markdown("<div class='weather-container'>", unsafe_allow_html=True)
            st.image(icon_url, width=80)  # Display Weather Icon
            st.success(f"**Weather in {city}:** {weather}")
            col1, col2, col3 = st.columns(3)
            col1.metric("🌡 Temperature", f"{temp}°C")
            col2.metric("💧 Humidity", f"{humidity}%")
            col3.metric("💨 Wind Speed", f"{wind_speed} km/h")
            st.markdown("</div>", unsafe_allow_html=True)
    
    else:
        st.error("❌ City not found. Please enter a valid city name.")

# 📌 Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #777;'>☀️ Stay Updated | Be Prepared | Enjoy the Weather ☀️</p>", unsafe_allow_html=True)


# curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=GEMINI_API_KEY"
# AIzaSyA2HjR8cihUSkLd_lbNkv72a_IScyrPIwg