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
