# Import necessary libraries 
from dash import html, dcc
import graphs
import tabfunc as tf
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from app import app
from dash.dependencies import Input, Output, State

country_list = ['Egypt','Algeria','Bahrain','Libyan Arab Jamahiriya','Jordan','Iraq','Mauritania','Morocco',
                  'Saudi Arabia','Kuwait','Qatar','Sudan (former)', 'Oman','Tunisia','United Arab Emirates','Yemen',
                  'Lebanon','Syrian Arab Republic','Somalia','Comoros','Djibouti']

t1_chart_radiobuttons = ["Region-wise distribution", "Population-GDP Correlation"]
t2_chart_radiobuttons = ["Basic Population Analysis", "Population Growth Analysis", "Population Value Table", "Annual Population Growth", "Population Growth Rate"]
t3_chart_radiobuttons = ["GDP per Capita Trend", "GDP per Capita Value"]
t4_chart_radiobuttons = ["Country-wise Trend for EF vs BC", "Entire UN Reion Ef vs BC Analysis", "Country-wise Deficit vs Reserve", "Ecological Deficit and GDP"]
t5_chart_radiobuttons = ["Earth Overshoot Day", "Carbon Footprint Analysis"]


top_card = dbc.Card(
    [
        dbc.CardBody(html.P("Please select the countries you wish to plot data for", className="card-text")),
        html.Div([
            dcc.Checklist(
                options = country_list,
                value = [],
                inline=True, style={"margin-left": "10px"}, inputStyle={"margin-right": "5px", "margin-left": "10px",
                                                                        "margin-bottom": "10px"},
                id = "country_checkbox"
            )
        ]),
        dbc.CardBody(html.P(" ", className="card-text"))
    ],
    style={"margin-left": "20px", "width": "45rem"},
)

bottom_card_1 = dbc.Card(
    [
        dbc.CardBody(html.P("Please select the charts you wish to view", className="card-text")),
        html.Div([
            dcc.RadioItems(
                options = t1_chart_radiobuttons,
                inline=True, style={"margin-left": "20px"}, inputStyle={"margin-right": "5px", "margin-left": "10px"},
                id = "chart_checkbox"
            ), 
        ],
            style={
                "height": "110px",
            },),
        dbc.CardBody(html.P(" ", className="card-text"))
    ],
    style={"margin-left": "5px", "width": "44rem"},
)

bottom_card_2 = dbc.Card(
    [
        dbc.CardBody(html.P("Please select the charts you wish to view", className="card-text")),
        html.Div([
            dcc.RadioItems(
                options = t2_chart_radiobuttons,
                inline=True, style={"margin-left": "20px"}, inputStyle={"margin-right": "5px", "margin-left": "10px"},
                id = "chart_checkbox"
            ), 
        ],
            style={
                "height": "110px",
            },),
        dbc.CardBody(html.P(" ", className="card-text"))
    ],
    style={"margin-left": "5px", "width": "44rem"},
)

bottom_card_3 = dbc.Card(
    [
        dbc.CardBody(html.P("Please select the charts you wish to view", className="card-text")),
        html.Div([
            dcc.RadioItems(
                options = t3_chart_radiobuttons,
                inline=True, style={"margin-left": "20px"}, inputStyle={"margin-right": "5px", "margin-left": "10px"},
                id = "chart_checkbox"
            ), 
        ],
            style={
                "height": "110px",
            },),
        dbc.CardBody(html.P(" ", className="card-text"))
    ],
    style={"margin-left": "5px", "width": "44rem"},
)

bottom_card_4 = dbc.Card(
    [
        dbc.CardBody(html.P("Please select the charts you wish to view", className="card-text")),
        html.Div([
            dcc.RadioItems(
                options = t4_chart_radiobuttons,
                inline=True, style={"margin-left": "20px"}, inputStyle={"margin-right": "5px", "margin-left": "10px"},
                id = "chart_checkbox"
            ), 
        ],
            style={
                "height": "110px",
            },),
        dbc.CardBody(html.P(" ", className="card-text"))
    ],
    style={"margin-left": "5px", "width": "44rem"},
)

bottom_card_5 = dbc.Card(
    [
        dbc.CardBody(html.P("Please select the charts you wish to view", className="card-text")),
        html.Div([
            dcc.RadioItems(
                options = t5_chart_radiobuttons,
                inline=True, style={"margin-left": "20px"}, inputStyle={"margin-right": "5px", "margin-left": "10px"},
                id = "chart_checkbox"
            ), 
        ],
            style={
                "height": "110px",
            },),
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
                            dbc.Tab(label='Basic Charts', tab_id='basic-charts', label_style={"font-weight": "bold", "color":"#079a82"}),
                            dbc.Tab(label='Population Visualizations', tab_id='pop-viz', label_style={"font-weight": "bold", "color":"#079a82"}),
                            dbc.Tab(label='GDP Visualizations', tab_id='gdp-viz', label_style={"font-weight": "bold", "color":"#079a82"}),
                            dbc.Tab(label='Footprint and Biocapacity', tab_id='footpr-bio', label_style={"font-weight": "bold", "color":"#079a82"}),
                            dbc.Tab(label='Others', tab_id='others', label_style={"font-weight": "bold", "color":"#079a82"})
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
                            dbc.Col(bottom_card_1),
                        ],
                    ),
                ),
                html.Div(
                    html.Button(style = white_button_style, id='submit-button-state', n_clicks=0, children='Submit'),
                ),
                html.Div(
                    id='graph-op1',
                    children = [],
                    style={'margin-top': '25px', 'display': 'flex', 'align-items':'center', 'justify-content':'center'}
                )
            ]
        )
    elif at == 'pop-viz':
        return html.Div(
            children = [
                html.Div(
                    children = dbc.Row(
                        [
                            dbc.Col(top_card),
                            dbc.Col(bottom_card_2),
                        ],
                    ),
                ),
                html.Div(
                    html.Button(style = white_button_style, id='submit-button-state', n_clicks=0, children='Submit'),
                ),
                html.Div(
                    id='graph-op1',
                    children = [],
                    style={'margin-top': '25px', 'display': 'flex', 'align-items':'center', 'justify-content':'center'}
                )
            ]
        )
    elif at == 'gdp-viz':
        return html.Div(
            children = [
                html.Div(
                    children = dbc.Row(
                        [
                            dbc.Col(top_card),
                            dbc.Col(bottom_card_3),
                        ],
                    ),
                ),
                html.Div(
                    html.Button(style = white_button_style, id='submit-button-state', n_clicks=0, children='Submit'),
                ),
                html.Div(
                    id='graph-op1',
                    children = [],
                    style={'margin-top': '25px', 'display': 'flex', 'align-items':'center', 'justify-content':'center'}
                )
            ]
        )
    elif at == 'footpr-bio':
        return html.Div(
            children = [
                html.Div(
                    children = dbc.Row(
                        [
                            dbc.Col(top_card),
                            dbc.Col(bottom_card_4),
                        ],
                    ),
                ),
                html.Div(
                    html.Button(style = white_button_style, id='submit-button-state', n_clicks=0, children='Submit'),
                ),
                html.Div(
                    id='graph-op1',
                    children = [],
                    style={'margin-top': '25px', 'display': 'flex', 'align-items':'center', 'justify-content':'center'}
                )
            ]
        )
    elif at == 'others':
        return html.Div(
            children = [
                html.Div(
                    children = dbc.Row(
                        [
                            dbc.Col(top_card),
                            dbc.Col(bottom_card_5),
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
                )
            ]
        )
    

@app.callback(
    Output("graph-op1", "children"), [Input("submit-button-state", "n_clicks")],
    State('country_checkbox', 'value'), State('chart_checkbox', 'value'), 
)

def show_selected_graphs(n_clicks, countrylist, graphlist):
    if (n_clicks):
        if graphlist in t1_chart_radiobuttons:
            return tf.tab1GraphsFunctionCall(graphlist, countrylist)
        elif graphlist in t2_chart_radiobuttons:
            return tf.tab2GraphsFunctionCall(graphlist, countrylist)
        elif graphlist in t3_chart_radiobuttons:
            return tf.tab3GraphsFunctionCall(graphlist, countrylist)
        elif graphlist in t4_chart_radiobuttons:
            return tf.tab4GraphsFunctionCall(graphlist, countrylist)
        