from dash import html, dcc
import dash_bootstrap_components as dbc
from src.config.settings import DEFAULT_TICKERS

layout = dbc.Container([
    html.H1("📈 Stock Market Dashboard"),

    dcc.Dropdown(
        id="ticker-dropdown",
        options=[{"label": t, "value": t} for t in DEFAULT_TICKERS],
        value=DEFAULT_TICKERS[0]
    ),

    dcc.Graph(id="price-chart"),
    dcc.Graph(id="volatility-chart")
])
