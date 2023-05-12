# Import necessary libraries 
from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app
from dash.dependencies import Input, Output


top_card = dbc.Card(
    [
        dbc.CardBody(html.P("Please select the countries you wish to plot data for", className="card-text")),
        dbc.CardBody(html.P("This card has an image at the top", className="card-text")),
    ],
    style={"margin-left": "20px", "width": "44rem"},
)

bottom_card = dbc.Card(
    [
        dbc.CardBody(html.P("Please select the charts you wish to view", className="card-text")),
        dbc.CardBody(html.P("This has a bottom image", className="card-text")),
    ],
    style={"margin-left": "5px", "width": "44rem"},
)


layout = html.Div(
    children = [
        html.Div(
            [dbc.Card(
            [
                dbc.CardHeader(
                    dbc.Tabs(
                        [
                            dbc.Tab(label='Basic Charts', tab_id='basic-charts'),
                            dbc.Tab(label='Population Visualizations', tab_id='tab-2'),
                            dbc.Tab(label='GDP Visualizations', tab_id='tab-3'),
                            dbc.Tab(label='Footprint and Biocapacity', tab_id='tab-4'),
                            dbc.Tab(label='Others', tab_id='tab-5')
                        ],
                        id="card-tabs",
                        active_tab="tab-1",
                    )
                ),
                dbc.CardBody(html.Div(id="card-content", className="mb-3")),
            ],style={"margin-left": "25px", "margin-right": "25px", "margin-top": "25px", "margin-bottom": "25px"}
        )
      ]
    ),
  ]
),


@app.callback(
    Output("card-content", "children"), [Input("card-tabs", "active_tab")]
)

def tab_content(at):
    if at == 'basic-charts':
        return html.Div(
            children = [
                html.Div(
                    children = dbc.Row(
                        [
                            dbc.Col(top_card),
                            dbc.Col(bottom_card),
                        ]
                    ),
                ),
                html.Div(
                    [
                        html.H3('Tab content 1'),
                        dcc.Graph(
                            figure={
                                'data': [{
                                    'x': [1, 2, 3],
                                    'y': [3, 1, 2],
                                    'type': 'bar'
                                }]
                            }
                        )
                    ]
                ),
            ]
        )
    else:
        return "This is tab {}".format(at)