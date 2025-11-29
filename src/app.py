from dash import Dash
import dash_bootstrap_components as dbc
from src.dashboard.layout import layout
from src.dashboard.callbacks import register_callbacks

def create_app():
    app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
    app.layout = layout
    register_callbacks(app)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
