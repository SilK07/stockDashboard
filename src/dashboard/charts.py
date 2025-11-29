import plotly.graph_objects as go

def price_chart(df, ticker):
    fig = go.Figure()
    
    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df["open"],
        high=df["high"],
        low=df["low"],
        close=df["close"],
        name="Price"
    ))
    
    fig.add_trace(go.Line(x=df.index, y=df["ma20"], name="MA20"))
    fig.add_trace(go.Line(x=df.index, y=df["ma50"], name="MA50"))

    fig.update_layout(title=f"{ticker} Price Chart", template="plotly_dark")
    return fig

def volatility_chart(df, ticker):
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df["volatility"],
        mode="lines",
        name="20-Day Volatility"
    ))
    
    fig.update_layout(
        title=f"{ticker} Volatility (20-Day Std Dev)",
        xaxis_title="Date",
        yaxis_title="Volatility",
        template="plotly_dark"
    )
    
    return fig

