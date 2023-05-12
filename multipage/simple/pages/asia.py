import dash_bootstrap_components as dbc
from dash import html

top_card = dbc.Card(
    [
        dbc.CardBody(html.P("Please select the countries you wish to plot data for", className="card-text")),
        dbc.CardBody(html.P("This card has an image at the top", className="card-text")),
    ],
    style={"margin-left": "38px", "width": "46rem"},
)

bottom_card = dbc.Card(
    [
        dbc.CardBody(html.P("Please select the charts you wish to view", className="card-text")),
        dbc.CardBody(html.P("This has a bottom image", className="card-text")),
    ],
    style={"margin-left": "22px", "width": "46rem"},
)

layout = html.Div(
    dbc.Row(
        [
            dbc.Col(top_card, width="auto"),
            dbc.Col(bottom_card, width="auto"),
        ]
    )
)