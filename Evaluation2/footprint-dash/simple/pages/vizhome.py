import graphs
from dash import dcc, html
from components import navbar

nav = navbar.Navbar()
layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="🌍", className="header-emoji"),
                html.H1(
                    children="Footprint Analytics", className="header-title"
                ),
                html.P(
                    children=(
                        "Analyze the behavior of resource utilization and how"
                        " that translates into the country's biocapacity and EF"
                    ),
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Data Points", className="menu-title"),
                        html.Div(
                            children="15K", className="menu-desc",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(children="Countries", className="menu-title"),
                        html.Div(
                            children="190", className="menu-desc",
                        ),
                    ],
                ),
                html.Div(
                    children=[
                        html.Div(
                            children="Years", className="menu-title"
                        ),
                        html.Div(
                            children="50+", className="menu-desc",
                        ),
                    ]
                ),
            ],
            className="menu",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                       figure = graphs.world_map()
                    ),
                    className="wrapper",
                ),
                html.Div(
                    # children=dcc.Graph(
                    #     id="volume-chart",
                    #     config={"displayModeBar": False},
                    # ),
                    className="card",
            ),
            ],
            className="wrapper",
        ),
    ]
)