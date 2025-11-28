import os 
from dotenv import load_dotenv

load_dotenv()

## API CONFIG
API_BASE_URL = os.getenv("API_BASE_URL")
LATITUDE = os.getenv("LATITUDE")
LONGITUDE = os.getenv("LONGITUDE")
HOURLY_FIELDS = os.getenv("HOURLY_FIELDS")


## DB CONFIG
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
