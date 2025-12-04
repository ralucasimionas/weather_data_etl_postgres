# WEATHER ETL & ANALYSIS PROJECT

## OVERVIEW

This project demonstrates a simple ETL(Extract, Transform, Load) pipeline for weather data using Python, Pandas and PostgreSQL.
It extract hourly weather data for 16 days from Open Meteo API, transforms it to remove empty values and duplicates and load it into a PostgreSQL database. Moreover, it calculates daily averages, min, max values. The project also includes visualizations of temperature and wind speed. Additionally, the ETL pipeline is fully **logged** using Python's `logging` module, providing information about each step of the process. This ensures easier debugging and monitoring of the pipeline.

## FEATURES

- Extract weather data (temperature, wind speed) for a given locations, based on latitude & longitude using Open Meteo API. You can use the standard coordinates or you can introduce your own.
- Transform data to remove empty values and duplicates.
- Load data into PostgreSQL table.
- Calculate daily average, min, max temperature & daily average wind speed.
- Generate visualizations:
  - current date's hourly temperature;
  - current date's hourly wind speed;
  - temperature forecast for 16 days, based on the average values of daily temperature;
  - wind speed forecast for 16 days, based on the average values of daily wind speed;
  - scatter plot of daily average temperature vs daily average wind speed for 16 days.
- Logging:
    - tracks each step of the ETL pipeline (extraction, transformation, database operations, visualizations)
    - logs any errors or exceptions with stack trace for easier debugging
    - saves logs both to console and to a log file

## TOOLS

- Python
- Pandas
- Matplotlib
- Requests
- Psycopg2
- PostgresSQL
- dotenv

## PROJECT STRUCTURE

weather*data_etl_postgres/
│
├── db_migrations/
│ ├── \_1_load_initial_data*.py # Load data into PostgreSQL
│ ├── \_2_rename_date_column.py # Rename data column function
│ └── \_3_add_columns_weather_table.py # Add new tables to table
├── src/
│ ├── config.py # Load environment variables
│ ├── extract.py # API data extraction
│ ├── main.py # Main ETL script
│ └── transform.py # Data transformation functions
│
├── visuals/ # Folder for saving plots
│ ├── hourly_temperature_today.png # Current date's hourly temperature forecast
│ ├── hourly_wind_speed_today.png # Current date's hourly speed wind forecast
│ ├── temperature_over_time.png # Temperature forecast for 16 days
│ ├── temperature_windSpeed_scatterplot.png # Scatter plot of daily average temperature vs daily
│ └── wind_speed_over_time.png # Wind speed forecast for 16 days
│
├── utils/ # Folder for util functions
│ ├── logger.py # Logger function
│ └── project.log # Logging details
│
├── .env # Environment variables (API key, DB credentials)
│
├── .gitignore  
│
├── requirements.txt  
│
├── README.md
