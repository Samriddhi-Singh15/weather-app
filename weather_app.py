# -*- coding: utf-8 -*-
"""weather-app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q72uEOlhBc0z7GBlwAuzg5uiZKKgeLTd
"""

import requests
while True:
  city=input("enter your city name:- (or write 'Exist' to quit) ").strip()
  if city.lower() == "exist":
    break
  api_key="2bd4518ca78d4dcbac6b136c3ca08f4c"
  responce=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
  data=responce.json()
  if data["cod"] !=200:
    print("wrong city girllll")
  else:
    temperature=data["main"]["temp"]
    feels_like=data["main"]["feels_like"]
    weather_condition=data["weather"][0]["main"]
    humidity=data["main"]["humidity"]
    wind_speed=data["wind"]["speed"]
    print(f"Temperature:{temperature} C")
    print(f"Feels like:{feels_like} C")
    print(f"Condition:{weather_condition}")

if weather_condition == "Clear":
    emoji = "☀️"
elif weather_condition == "Clouds":
    emoji = "☁️"
elif weather_condition == "Rain":
    emoji = "🌧️"
elif weather_condition == "Thunderstorm":
    emoji = "⛈️"
elif weather_condition == "Snow":
    emoji = "❄️"
elif weather_condition == "Haze" or weather_condition == "Mist":
    emoji = "🌫️"
else:
    emoji = "🌈"

print(f"🌡️ Temperature: {temperature}°C")
print(f"🤔 Feels Like: {feels_like}°C")
print(f"🌥️ Condition: {weather_condition} {emoji}")
print(f"💧 Humidity: {humidity}%")
print(f"💨 Wind Speed: {wind_speed} m/s")