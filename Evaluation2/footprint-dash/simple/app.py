import pandas as pd
import graphs
import numpy as np
import plotly.graph_objs as go
import plotly.offline as py
from plotly import tools
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from components import navbar

app = Dash(__name__,
           external_stylesheets=[dbc.themes.BOOTSTRAP],
           suppress_callback_exceptions=True)

# if __name__ == "__main__":
#     app.run_server(debug=True)