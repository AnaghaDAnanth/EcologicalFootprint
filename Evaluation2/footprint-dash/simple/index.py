import pandas as pd
import graphs
from app import app
import numpy as np
import plotly.graph_objs as go
import plotly.offline as py
from plotly import tools
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from components import navbar

from pages import arab, asia, europe, vizhome

data = (
    pd.read_csv("avocado.csv")
    .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
)
regions = data["region"].sort_values().unique()
avocado_types = data["type"].sort_values().unique()

external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]

app.title = "Footprint Analytics: Understand Your Ecological Footprint!"

nav = navbar.Navbar()
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav, 
    html.Div(id='page-content', children=[]), 
])

# Create the callback to handle mutlipage inputs
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/arab':
        return arab.layout
    if pathname == '/asia':
        return asia.layout
    if pathname == '/europe':
        return europe.layout
    else: # if redirected to unknown link
        return vizhome.layout


if __name__ == "__main__":
    app.run_server(debug=True)