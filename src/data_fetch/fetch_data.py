import yfinance as yf
import pandas as pd
from src.config.settings import RAW_DIR, DEFAULT_TICKERS

def fetch_market_data(tickers=DEFAULT_TICKERS, period="1y", interval="1d"):
    for ticker in tickers:
        df = yf.download(ticker, period=period, interval=interval)

        # Reset index so Date is a column
        df = df.reset_index()

        # Add ticker column
        df["Ticker"] = ticker

        # Save clean CSV (NO bad header rows)
        df.to_csv(f"{RAW_DIR}{ticker}.csv", index=False)

    print("✔ Clean market data saved!")
