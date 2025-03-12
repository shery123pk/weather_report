import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Set Page Config
st.set_page_config(
    page_title="Simple Weather App 🌦️",
    page_icon="🌎",
    layout="centered"
)

# Custom CSS for Styling
st.markdown("""
    <style>
        /* Background Image */
        body {
            background-image: url('https://source.unsplash.com/1600x900/?sky,clouds,city');
            background-size: cover;
            background-attachment: fixed;
            font-family: 'Arial', sans-serif;
        }

        /* Title Styling */
        .title {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            color: #ffffff;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
        }

        /* Input Box Styling */
        .stTextInput > div > div > input {
            border-radius: 10px;
            border: 2px solid #ffcc00;
            background-color: rgba(255, 255, 255, 0.9); /* Light background */
            color: black !important; /* Black text */
        }

        /* Weather Card */
        .weather-card {
            background: rgba(0, 0, 0, 0.6);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            color: white;
            box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.2);
        }

        /* Footer */
        .footer {
            text-align: center;
            font-size: 14px;
            color: #dddddd;
        }
    </style>
""", unsafe_allow_html=True)

# App Title with Styling
st.markdown('<h1 class="title">🌍 Fancy Weather App 🌦️</h1>', unsafe_allow_html=True)

# User Input for City Name
city = st.text_input("🏙️ Enter a city name:", placeholder="E.g., New York, Tokyo, Paris")

# Fetch Weather Data
if st.button("🔍 Check Weather"):
    if city:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            condition = data['weather'][0]['description']
            icon_code = data['weather'][0]['icon']
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"

            # Display Weather Information with Card Styling
            st.markdown(f"""
                <div class="weather-card">
                    <h2>🌆 {city.capitalize()}</h2>
                    <img src="{icon_url}" width="100">
                    <h3>🌡️ Temperature: <span style="color: #ffcc00;">{temp}°C</span></h3>
                    <h3>💧 Humidity: <span style="color: #00ccff;">{humidity}%</span></h3>
                    <h3>🌤️ Condition: <span style="color: #ff9999;">{condition.capitalize()}</span></h3>
                </div>
            """, unsafe_allow_html=True)

        else:
            st.error("🚨 City not found! Please enter a valid city name.")

# Footer
st.markdown('<p class="footer">Made with ❤️ using Streamlit</p>', unsafe_allow_html=True)
