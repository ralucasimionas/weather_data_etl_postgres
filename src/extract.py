import requests 
import pandas as pd 
from config import API_BASE_URL, LATITUDE, LONGITUDE, HOURLY_FIELDS, FORECAST_DAYS

def extract_weather_data():

    print(f"Default coordinates: Latitude={LATITUDE}, Longitude={LONGITUDE}")

    use_default = input("Do you want to use the default coordinates? (y/n): ").strip().lower()

    if use_default == 'n':
        try: 
            latitude = float(input("Enter latitude: ").strip())
            longitude = float(input("Enter longitude: ").strip())

        except ValueError:
            print("Invalid input. Using default coordinates.")
            latitude = LATITUDE
            longitude = LONGITUDE
        
    else:
            latitude = LATITUDE
            longitude = LONGITUDE

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "forecast_days": FORECAST_DAYS,
        "hourly": HOURLY_FIELDS
    }

    response = requests.get(API_BASE_URL, params=params)

    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")
    

    data = response.json()

    if "hourly" not in data:
        raise Exception(f"No 'hourly' data found. Response: {data}")
    
    print(f"Data successfully extracted for Latitude={latitude}, Longitude={longitude}")

    df = pd.DataFrame({
        "date": data["hourly"]["time"],
        "temperature": data["hourly"]["temperature_2m"],
        "wind_speed": data["hourly"]["wind_speed_10m"],
    })

    return df