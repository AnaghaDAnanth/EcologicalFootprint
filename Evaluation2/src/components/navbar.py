# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc


# Define the navbar structure
def Navbar():

    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Arab", href="/arab", style={"font-weight": "bold","color":"#ffffff"})),
                dbc.NavItem(dbc.NavLink("Asia", href="/asia", style={"font-weight": "bold","color":"#ffffff"})),
                dbc.NavItem(dbc.NavLink("Europe", href="/europe", style={"font-weight": "bold","color":"#ffffff"})),
                dbc.NavItem(dbc.NavLink("America", href="/america", style={"font-weight": "bold","color":"#ffffff"})),
            ] ,
            brand="📈 Biocapacity and EF Analysis",
            brand_href="/vizhome",
            color="rgb(53, 153, 134)",
            dark=True
        ), 
    ])

    return layout