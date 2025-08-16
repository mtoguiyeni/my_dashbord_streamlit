# transform.py
import pandas as pd


def clean_data(df):
    df["date"] = pd.to_datetime(df["date"])
    df = df[df["value"] > 0]
    return df
