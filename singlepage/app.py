import pandas as pd
import graphs
import numpy as np
import plotly.graph_objs as go
import plotly.offline as py
from plotly import tools
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc


external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]

app = Dash(__name__)

#------------------------------------------------------------------------------------------#
#-------------------------------------------DASH-------------------------------------------#
#------------------------------------------------------------------------------------------#
app.layout = html.Div(
    children=[
        html.H1(children="Biocapacity and EF Analysis"),
        html.P(
            children=(
                "Analyze the behavior of avocado prices and the number"
                " of avocados sold in the US between 2015 and 2018"
            ),
        ),
        dcc.Tabs(id="tabs-example-graph", value='notab-content', children=[
        dcc.Tab(label='Basic Charts', value='tab-1'),
        dcc.Tab(label='Population Visualizations', value='tab-2'),
        dcc.Tab(label='GDP Visualizations', value='tab-3'),
        dcc.Tab(label='Footprint and Biocapacity', value='tab-4'),
        dcc.Tab(label='Others', value='tab-5')
        ]),
        dcc.Graph(
            figure={
                "data": graphs.graph_1()[0],
                "layout": graphs.graph_1()[1]
            },
        ),
        dcc.Graph(
            figure={
                "data": graphs.graph_2()[0],
                "layout": graphs.graph_2()[1]
            },
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
