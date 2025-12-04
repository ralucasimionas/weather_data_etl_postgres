import psycopg2

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))
sys.path.append(str(Path(__file__).resolve().parent.parent / "utils"))

from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

from logger import setup_logger # type: ignore
logger = setup_logger(__name__)


def load_data_to_postgres(df):
    try:
            logger.info("Starting initial data load into PostgreSQL.")

            with psycopg2.connect(
                host=DB_HOST,
                port=DB_PORT,
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            ) as conn:
                with conn.cursor() as cursor:

                    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS weather_recordings (
                        date TIMESTAMP,
                        temperature FLOAT,
                        wind_speed FLOAT
                    );
                    """)

                    logger.info("Checked/created table weather_recordings.")

                    for index, row in df.iterrows():
                        cursor.execute(
                            """
                            INSERT INTO weather_recordings (date, temperature, wind_speed)
                            VALUES (%s, %s, %s)
                            """,
                            (row['date'], row['temperature'], row['wind_speed'])
                        )

                    logger.info(f"Inserted {len(df)} rows into weather_recordings table.")

    except Exception as e:
                logger.error(f"Error loading data to PostgreSQL: {e}", exc_info=True)  
                raise

 