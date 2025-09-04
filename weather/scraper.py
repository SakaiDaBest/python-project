from flask import Flask
import pandas as pd
import requests
import json
from datetime import datetime
import os
from sqlalchemy import create_engine

open("weather_info.csv", "w").close()

def weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=3fe71e0afb5c99b243dcbb2cdbf41742"
    response = requests.get(url)
    data = response.json()

    info = {
        "city": data.get('name'),
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature_c": round(data.get('main').get('temp'), 1),
        "feels_like_c": round(data.get('main').get('feels_like'), 1),
        "humidity": data.get('main').get('humidity'),
        "pressure": data.get('main').get('pressure'),
        "wind_speed_mps": data.get('wind').get('speed'),
        "wind_direction_deg": data.get('wind').get('deg'),
        "weather_desc": data.get('weather')[0].get('description').lower(),
        "cloudiness_pct": data.get('clouds').get('all')
    }

    df = pd.DataFrame([info])
    df.to_csv('weather_info.csv', mode='a', header=not os.path.exists("weather_info.csv") or os.stat("weather_info.csv").st_size == 0, index=False)

cities = ["Kuala Lumpur", "Ampang"]
for city in cities:
    weather(city)

df_all = pd.read_csv('weather_info.csv')
engine = create_engine('sqlite:///weather.db')
df_all.to_sql('weather', con=engine, if_exists='replace', index=False)