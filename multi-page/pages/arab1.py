# Import necessary libraries 
from dash import html, dcc
import graphs
import dash_bootstrap_components as dbc
from app import app
from dash.dependencies import Input, Output, State

country_list = ['New York City', 'Montréal', 'San Francisco']

top_card = dbc.Card(
    [
        dbc.CardBody(html.P("Please select the countries you wish to plot data for", className="card-text")),
        html.Div([
            dcc.Checklist(
                options = country_list,
                value = [],
                inline=True, style={"margin-left": "20px"}, inputStyle={"margin-right": "5px", "margin-left": "10px"},
                id = "country_checkbox"
            )
        ]),
        dbc.CardBody(html.P(" ", className="card-text"))
    ],
    style={"margin-left": "20px", "width": "44rem"},
)

bottom_card = dbc.Card(
    [
        dbc.CardBody(html.P("Please select the charts you wish to view", className="card-text")),
        html.Div([
            dcc.Checklist(
                options = country_list,
                value = [],
                inline=True, style={"margin-left": "20px"}, inputStyle={"margin-right": "5px", "margin-left": "10px"},
                id = "chart_checkbox"
            )
        ]),
        dbc.CardBody(html.P(" ", className="card-text"))
    ],
    style={"margin-left": "5px", "width": "44rem"},
)

white_button_style = {'background-color': 'cream', 'border-color': '#079a82',
                      'color': 'black', 'height': '30px',
                      'width': '100px', 'margin-top': '10px',
                      'margin-left': '705px', 'border-radius': '10px' }

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
    # html.Div(
    #     children=
    #         dcc.Graph(
    #             figure = graphs.world_map()),
    #         className="card",
    # )
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
                        ],
                    ),
                ),
                html.Div(
                    html.Button(style = white_button_style, id='submit-button-state', n_clicks=0, children='Submit'),
                ),
                html.Div(
                    id='graph-op1',
                    children = [],
                    # style={'display': 'flex'}
                ),
                html.Div(
                    id='graph-op2',
                    children = [],
                    # style={'display': 'flex'}
                ),
                html.Div(
                    id='graph-op3',
                    children = [],
                    # style={'display': 'flex'}
                ),
            ]
        )
    else:
        return "Select a tab to visualize the charts!"
    

@app.callback(
    Output("graph-op1", "children"), Input("submit-button-state", "n_clicks")
)

def show_selected_graphs(n_clicks):
    if (n_clicks):
        return dcc.Graph(id='display-map', figure=graphs.world_map())