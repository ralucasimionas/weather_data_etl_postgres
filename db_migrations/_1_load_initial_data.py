import psycopg2

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

def load_data_to_postgres(df):
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather_recordings (
        date TIMESTAMP,
        temperature FLOAT,
        wind_speed FLOAT
    );
    """)

    for index, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO weather_recordings (date, temperature, wind_speed)
            VALUES (%s, %s, %s)
            """,
            (row['date'], row['temperature'], row['wind_speed'])
        )

    conn.commit()
    cursor.close()
    conn.close()