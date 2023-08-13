# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc


# Define the navbar structure
def Navbar():

    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Arab", href="/arab")),
                dbc.NavItem(dbc.NavLink("Asia", href="/asia")),
                dbc.NavItem(dbc.NavLink("Europe", href="/arab")),
                dbc.NavItem(dbc.NavLink("UN Regions", href="/arab")),
            ] ,
            brand="Biocapacity and EF Analysis",
            brand_href="/home",
            color="dark",
            dark=True,
        ), 
    ])

    return layout