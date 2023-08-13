# Tutorial for multi page - https://levelup.gitconnected.com/creating-a-multi-page-dash_application-ab38b4b91bf5

from dash import html, dcc
from dash.dependencies import Input, Output
import dash
import dash_bootstrap_components as dbc
# Connect to your app pages
from pages import arab, asia, home
# Connect the navbar to the index
from components import navbar

def dash_page_index():
    app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.BOOTSTRAP], 
                meta_tags=[{"name": "viewport", "content": "width=device-width"}],
                suppress_callback_exceptions=True)
    # Define the navbar
    nav = navbar.Navbar()
    # Define the index page layout
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
        else: # if redirected to unknown link
            return home.layout

    # Run the dash_app on localhost:8050
    if __name__ == '__main__':
        app.run_server(debug=True)

dash_page_index()