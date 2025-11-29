import pandas as pd

def clean(df):
    df = df.copy()
    df = df.dropna()
    df.columns = [c.lower() for c in df.columns]
    df.index = pd.to_datetime(df.index)
    return df
