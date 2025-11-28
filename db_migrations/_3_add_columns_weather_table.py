import psycopg2
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD


conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    
cursor = conn.cursor()



cursor.execute("""
    ALTER TABLE weather_recordings
    ADD COLUMN IF NOT EXISTS latitude FLOAT,
    ADD COLUMN IF NOT EXISTS longitude FLOAT;
    """)

conn.commit()
cursor.close()
conn.close()

print("Migration completed successfully.")