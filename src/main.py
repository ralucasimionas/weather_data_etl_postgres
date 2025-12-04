from extract import extract_weather_data
from transform import transform_weather_data, get_daily_average

import sys
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parent.parent / "db_migrations"))
sys.path.append(str(Path(__file__).resolve().parent.parent / "utils"))

from _1_load_initial_data import load_data_to_postgres # type: ignore
from logger import setup_logger # type: ignore
logger = setup_logger(__name__)


try: 
    logger.info("ETL process started.")
    df = extract_weather_data()
    df = transform_weather_data(df)
    daily_average = get_daily_average(df)
    load_data_to_postgres(df)

    currentDate = pd.Timestamp.now().date()
    formattedDate = currentDate.strftime("%A, %d-%m-%Y")

    start_date = daily_average['date'].min().strftime("%d-%m-%Y")
    end_date = daily_average['date'].max().strftime("%d-%m-%Y")
    ###  Visualize the data
    ## Temperature/Wind speed over time
    plt.figure(figsize=(12,6))
    plt.plot(daily_average['date'], daily_average['avg_temp'], marker='o', markersize=4, color='orange')
    plt.title(f"Daily Temperature Forecast from {start_date} to {end_date}")
    plt.xlabel("Date") 
    plt.ylabel("Temperature (°C)")
    plt.xticks(daily_average['date'], rotation=45)  

    plt.savefig("../visuals/temperature_over_time.png")
    # plt.show()


    plt.figure(figsize=(12,6))
    plt.plot(daily_average["date"], daily_average["avg_wind_speed"], marker='*', markersize=4, color='green')
    plt.title(f"Daily Wind Speed Forecast from {start_date} to {end_date}")
    plt.xlabel("Date")
    plt.ylabel("Wind Speed (km/h)")
    plt.xticks(daily_average['date'], rotation=45)  

    plt.savefig("../visuals/wind_speed_over_time.png")
    # plt.show()

    ## Hourly Plot for current date



    todaysData = df[df['date'].dt.date == currentDate].copy()
    todaysData['hour'] =  todaysData['date'].dt.hour 

    plt.figure(figsize=(12,6))
    plt.plot(todaysData['hour'], todaysData['temperature'], label='Temperature (°C)', marker='o', markersize=4, color='blue', markeredgewidth=2)
    plt.title(f"Hourly Temperature for Today, {formattedDate} ")
    plt.xlabel("Hour")
    plt.ylabel("Values")
    plt.xticks(range(0,24))
    plt.legend()
    plt.savefig("../visuals/hourly_temperature_today.png")
    # plt.show()


    plt.figure(figsize=(12,6))
    plt.plot(todaysData['hour'], todaysData['wind_speed'], label='Wind Speed (km/h)', marker='s', markersize=4, color='blue', markeredgewidth=2)
    plt.title(f"Hourly Wind Speed for Today, {formattedDate} ")
    plt.xlabel("Hour")
    plt.ylabel("Values")
    plt.xticks(range(0,24))
    plt.legend()
    plt.savefig("../visuals/hourly_wind_speed_today.png")
    # plt.show()

    ## Daily Average Scatter Plots
    print(daily_average.head(10))
    plt.figure(figsize=(12,6))
    plt.scatter(daily_average['avg_temp'], daily_average['avg_wind_speed'], color='blue', s=100, edgecolor='k')
    plt.xlabel("Average Temperature (°C)")
    plt.ylabel("Average Wind Speed (km/h)")
    plt.title(f"Daily Avg Temperature vs Wind Speed  from {start_date} to {end_date}") 
    plt.grid(True)
    plt.savefig("../visuals/temperature_windSpeed_scatterplot.png")
    plt.show()

    logger.info("ETL process completed and visualizations saved.")

except Exception as e:
    logger.error(f"ETL process failed: {e}", exc_info=True)
    raise
