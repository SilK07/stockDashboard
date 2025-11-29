def add_indicators(df):
    df["ma20"] = df["close"].rolling(20).mean()
    df["ma50"] = df["close"].rolling(50).mean()
    df["volatility"] = df["close"].pct_change().rolling(20).std()
    return df
