from dash import Input, Output
from src.dashboard.charts import price_chart, volatility_chart
from src.processing.clean_data import clean
from src.processing.indicators import add_indicators
import pandas as pd

def register_callbacks(app):

    @app.callback(
        [
            Output("price-chart", "figure"),
            Output("volatility-chart", "figure")
        ],
        Input("ticker-dropdown", "value")
    )
    def update_charts(ticker):
        df = pd.read_csv(f"data/raw/{ticker}.csv")

        # Fix hidden BOM, lowercase all headers
        df.columns = (
            df.columns
            .str.replace('\ufeff', '', regex=True)
            .str.strip()
            .str.lower()
        )

        # Safety check for date column
        if "date" not in df.columns:
            print("COLUMNS:", df.columns.tolist())
            raise KeyError("Date column not found. Check fetch_data().")

        # Parse date
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df = df.dropna(subset=["date"])
        df = df.set_index("date")

        # Convert numeric columns
        numeric_cols = ["open", "high", "low", "close", "volume"]
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        # Run cleaning + technical indicators
        df = clean(df)
        df = add_indicators(df)

        # Generate both charts
        price_fig = price_chart(df, ticker)
        vol_fig = volatility_chart(df, ticker)

        return price_fig, vol_fig
