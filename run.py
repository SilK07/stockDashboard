from src.data_fetch.fetch_data import fetch_market_data
from src.app import app

if __name__ == "__main__":
    fetch_market_data()
    app.run(debug=True)
