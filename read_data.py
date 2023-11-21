import pandas as pd
import os


def download_data_from_url(url):
    df = pd.read_csv(url)
    return df


def save_data_to_file(df, path):
    if not os.path.exists("data"):
        os.makedirs("data")
    df.to_csv(path)

def read_data(url, path):
    df = download_data_from_url(url)
    save_data_to_file(df, path)

def read_file(path):
    return pd.read_csv(path)

def save_data_to_db(conn, path):
    df = pd.read_csv(path)
    df.to_sql('weather', conn, if_exists='replace', index=False)
    return conn

def read_data_from_sql(conn):
    df = pd.read_sql_query('weather', conn, index_col=None, coerce_float=True, params=None, parse_dates=None, chunksize=None)
    return df