import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

st.set_page_config(page_title="Weather App", page_icon="🌦️")

st.title("🌦️ Weather App")
st.write("Enter your city name and click the button to get the wheather")

city = st.text_input("Enter the City Name : ")
API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"      # Dynamic API URL

if st.button("Fetch Weather Data"):                                                                     # Button to get data
    response = requests.get(API_URL)
    
    if(response.status_code == 200):
        st.success("Data fetch successfully")
        data = response.json()

        st.metric("Temperature : ",f"{data['main']['temp']}")
        st.metric("Feels_Like : ", f"{data['main']['feels_like']}")
        st.metric("Humidity ; ", f"{data['main']['humidity']}")
        st.metric("Wind Speed ; ", f"{data['wind']['speed']}")

        name = data["name"]
        country = data["sys"]["country"]
        st.subheader(f"Weather data for {city}")
            
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather = data["weather"][0]["main"]

        col1, col2, col3, col4 = st.columns(4)
      
        col1.metric("Temperature", f"🌡️{data['main']['temp']} °C")
        col2.metric("Humidity", f"💧{humidity}%")
        col3.metric("Wind Speed", f"🍃{wind_speed} m/s")
        col4.metric("Weather", f"☀️{weather}")

    else:
        st.error("Invalid city name")