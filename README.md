# WEATHER ETL & ANALYSIS PROJECT

## OVERVIEW
This project demonstrates a simple ETL(Extract, Transform, Load) pipeline for weather data using Python, Pandas and PostgreSQL. 
It extract hourly weather data for 16 days from Open Meteo API, transforms it to remove empty values and duplicates and load it into a PostgreSQL database. Moreover, it calculates daily averages, min, max values. The project also includes visualizations of temperature and wind speed.


## FEATURES
- Extract weather data (temperature, wind speed) for a given locations, based on latitude & longitude using Open Meteo API.
- Transform data to remove empty values and duplicates.
- Load data into PostgreSQL table.
- Calculate daily average, min, max temperature & daily average wind speed.
- Generate visualizations:
    - current date's hourly temperature;
    - current date's hourly wind speed;
    - temperature forecast for 7 days, based on the average values of daily temperature;
    - wind speed forecast for 7 days, based on the average values of daily wind speed;
    - scatter plot of daily average temperature vs daily average wind speed for 7 days.


## TOOLS
- Python
- Pandas
- Matplotlib
- Requests
- Psycopg2
- PostgresSQL
- dotenv


## PROJECT STRUCTURE

weather_data_etl_postgres/
│
├── src/
│   ├── config.py                                       # Load environment variables
│   ├── extract.py                                      # API data extraction
│   ├── load.py                                         # Load data into PostgreSQL
│   ├── main.py                                         # Main ETL script
│   ├── rename_column.py                                # Rename table column function
│   └── transform.py                                    # Data transformation functions
│
├── visuals/                                            # Folder for saving plots
│   ├── hourly_temperature_today.png                    # Current date's hourly temperature forecast
│   ├── hourly_wind_speed_today.png                     # Current date's hourly speed wind forecast
│   ├── temperature_over_time.png                       # Temperature forecast for 7 days
│   ├── temperature_windSpeed_scatterplot.png           # Scatter plot of daily average temperature vs daily average wind speed
│   └── wind_speed_over_time.png                        # Wind speed forecast for 7 days
│
├── .env                                                # Environment variables (API key, DB credentials)
│
├── .gitignore                                            
│
├── requirements.txt                                        
│
├── README.md                                           


