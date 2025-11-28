import requests 
import pandas as pd 
from config import API_BASE_URL, LATITUDE, LONGITUDE, HOURLY_FIELDS

def extract_weather_data():
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "forecast_days": 16,
        "hourly": HOURLY_FIELDS
    }

    response = requests.get(API_BASE_URL, params=params)

    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")
    

    data = response.json()

    if "hourly" not in data:
        raise Exception(f"No 'hourly' data found. Response: {data}")
    

    df = pd.DataFrame({
        "date": data["hourly"]["time"],
        "temperature": data["hourly"]["temperature_2m"],
        "wind_speed": data["hourly"]["wind_speed_10m"],
    })

    return df