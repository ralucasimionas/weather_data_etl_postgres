import psycopg2
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))
sys.path.append(str(Path(__file__).resolve().parent.parent / "utils"))
from logger import setup_logger # type: ignore

from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD


logger = setup_logger(__name__)
try:
     logger.info("Starting migration to add latitude and longitude columns.")

     with psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    ) as conn:
          with conn.cursor() as cursor:

            add_columns_query = ("""
                ALTER TABLE weather_recordings
                ADD COLUMN IF NOT EXISTS latitude FLOAT,
                ADD COLUMN IF NOT EXISTS longitude FLOAT;
                """)

            cursor.execute(add_columns_query)
            logger.info("Columns 'latitude' and 'longitude' have been successfully added to 'weather_recordings' table.")   
except Exception as e:
        logger.error(f"Error during adding columns migration: {e}", exc_info=True)    
        raise