from extract import extract_weather_data
from transform import transform_weather_data, get_daily_average
from load import load_data_to_postgres
import matplotlib.pyplot as plt
import pandas as pd

df = extract_weather_data()
df = transform_weather_data(df)
daily_average = get_daily_average(df)
load_data_to_postgres(df)

###  Visualize the data
## Temperature/Wind speed over time
plt.figure(figsize=(8,6))
plt.plot(daily_average['date'], daily_average['avg_temp'], marker='o', color='orange')
plt.title("Daily Temperature Forecast")
plt.xlabel("Date") 
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)  
plt.tight_layout()
plt.savefig("../visuals/temperature_over_time.png")
# plt.show()

plt.figure()
plt.figure(figsize=(8,6))
plt.plot(daily_average["date"], daily_average["avg_wind_speed"], marker='*', color='green')
plt.title("Daily Wind Speed Forecast")
plt.xlabel("Date")
plt.ylabel("Wind Speed (km/h)")
plt.xticks(rotation=45)  
plt.tight_layout()
plt.savefig("../visuals/wind_speed_over_time.png")
# plt.show()

## Hourly Plot for current date
today = df[df['date'].dt.date == pd.Timestamp.now().date()].copy()
today['hour'] =  today['date'].dt.hour 
plt.figure(figsize=(8,6))
plt.plot(today['hour'], today['temperature'], label='Temperature (°C)', marker='o', markersize=2, color='blue', markeredgewidth=2)
plt.title("Hourly Weather for Today ")
plt.xlabel("Hour")
plt.ylabel("Values")
plt.xticks(range(0,24))
plt.legend()
plt.savefig("../visuals/hourly_temperature_today.png")
# plt.show()


today = df[df['date'].dt.date == pd.Timestamp.now().date()].copy()
today['hour'] =  today['date'].dt.hour 
plt.figure(figsize=(8,6))
plt.plot(today['hour'], today['wind_speed'], label='Wind Speed (km/h)', marker='s', markersize=2, color='blue', markeredgewidth=2)
plt.title("Hourly Wind Speed for Today ")
plt.xlabel("Hour")
plt.ylabel("Values")
plt.xticks(range(0,24))
plt.legend()
plt.savefig("../visuals/hourly_wind_speed_today.png")
# plt.show()

## Daily Average Plots
print(daily_average.head(10))
plt.figure(figsize=(8,6))
plt.scatter(daily_average['avg_temp'], daily_average['avg_wind_speed'], color='blue', s=100, edgecolor='k')
plt.xlabel("Average Temperature (°C)")
plt.ylabel("Average Wind Speed (km/h)")
plt.title("Daily Avg Temperature vs Wind Speed (Last 7 Days)")
plt.grid(True)
plt.savefig("../visuals/temperature_windSpeed_scatterplot.png")
plt.show()

print("ETL process completed and visualizations saved.")
