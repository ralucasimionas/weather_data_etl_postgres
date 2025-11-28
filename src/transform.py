import pandas as pd

def transform_weather_data(df):
    df['date'] = pd.to_datetime(df['date'])
    df=df.dropna()

   
    return df


def get_daily_average(df):
    daily_average = df.groupby(df['date'].dt.date).agg(
        avg_temp = ('temperature', 'mean'),
        avg_wind_speed = ('wind_speed', 'mean'),
        min_temp =('temperature', 'min'),
        max_temp =('temperature', 'max')).reset_index()

    daily_average.rename(columns={'date': 'date'}, inplace=True)
    return daily_average