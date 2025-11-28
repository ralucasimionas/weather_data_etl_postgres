import pandas as pd

def transform_weather_data(df):
    df['date'] = pd.to_datetime(df['date'])
    df=df.dropna()
    df=df.drop_duplicates()
    df = df.sort_values(by='date', ascending=False).reset_index(drop=True)
    return df


def get_daily_average(df):
    daily_average = df.groupby(df['date'].dt.date).agg(
        avg_temp = ('temperature', 'mean'),
        avg_wind_speed = ('wind_speed', 'mean'),
        min_temp =('temperature', 'min'),
        max_temp =('temperature', 'max')).reset_index()

    daily_average.rename(columns={'date': 'date'}, inplace=True)
    daily_average = daily_average.drop_duplicates(subset=['date'])
    daily_average = daily_average.sort_values(by='date', ascending=False).reset_index(drop=True)
    return daily_average