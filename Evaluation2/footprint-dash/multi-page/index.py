# Tutorial for multi page - https://levelup.gitconnected.com/creating-a-multi-page-dash-application-ab38b4b91bf5

from dash import html, dcc
from dash.dependencies import Input, Output
# Connect to main app.py file
from app import app
# Connect to your app pages
from pages import arab, asia, home
# Connect the navbar to the index
from components import navbar

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

# Run the app on localhost:8050
if __name__ == '__main__':
    app.run_server(debug=True)