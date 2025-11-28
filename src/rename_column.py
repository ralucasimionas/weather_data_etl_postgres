import psycopg2
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD


conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
cursor = conn.cursor()

rename_query = ("""
    ALTER TABLE weather_recordings 
    RENAME COLUMN time TO date;
    """)

cursor.execute(rename_query)

conn.commit()
cursor.close()
conn.close()

print("Column 'time' has been successfully renamed to 'date' in 'weather_recordings' table.")