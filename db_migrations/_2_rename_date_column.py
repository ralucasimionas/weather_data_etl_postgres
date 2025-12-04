import psycopg2
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "utils"))
rom logger import setup_logger # type: ignore
logger = setup_logger(__name__)

try:
     logger.info("Starting column rename migration: time to date.")

     with psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    ) as conn:
          with conn.cursor() as cursor:

            rename_query = ("""
                ALTER TABLE weather_recordings 
                RENAME COLUMN time TO date;
                """)

            cursor.execute(rename_query)
            logger.info("Column 'time' has been successfully renamed to 'date' in 'weather_recordings' table.")

except Exception as e:
        logger.error(f"Error during column rename migration: {e}", exc_info=True)    
        raise  