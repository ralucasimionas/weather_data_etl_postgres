import pandas as pd
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent / "utils"))
from logger import setup_logger # type: ignore
logger = setup_logger(__name__)

def transform_weather_data(df):
    logger.info("Starting data transformation.")
    
    try:
        df['date'] = pd.to_datetime(df['date'])
        df=df.dropna()
        df=df.drop_duplicates()
        df = df.sort_values(by='date', ascending=False).reset_index(drop=True)
        return df
    except Exception as e:
        logger.error(f"Error during data transformation: {e}")
        raise


def get_daily_average(df):
    logger.info("Calculating daily averages.")
    try:
        daily_average = df.groupby(df['date'].dt.date).agg(
            avg_temp = ('temperature', 'mean'),
            avg_wind_speed = ('wind_speed', 'mean'),
            min_temp =('temperature', 'min'),
            max_temp =('temperature', 'max')).reset_index()

        daily_average.rename(columns={'date': 'date'}, inplace=True)
        daily_average = daily_average.drop_duplicates(subset=['date'])
        daily_average = daily_average.sort_values(by='date', ascending=False).reset_index(drop=True)
        return daily_average
    except Exception as e:
        logger.error(f"Error calculating daily averages: {e}", exc_info=True)
        raise