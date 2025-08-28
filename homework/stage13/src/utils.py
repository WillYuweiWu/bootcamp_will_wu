import pandas as pd
import re

def parse_dates(df: pd.DataFrame, columns) -> pd.DataFrame:
    df_copy = df.copy()
    for col in columns:
        df_copy[col] = pd.to_datetime(df_copy[col], errors='coerce')
    return df_copy


def calculate_metrics(df):
    return df.describe()
