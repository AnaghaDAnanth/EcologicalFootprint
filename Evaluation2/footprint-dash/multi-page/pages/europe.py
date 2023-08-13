import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.offline as py
from plotly import tools
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

arab_df = pd.read_csv("pages/Arab.csv")

arab_countries = ['Egypt','Algeria','Bahrain','Libyan Arab Jamahiriya','Jordan','Iraq','Mauritania','Morocco',
                  'Saudi Arabia','Kuwait','Qatar','Sudan (former)', 'Oman','Tunisia','United Arab Emirates','Yemen',
                  'Lebanon','Syrian Arab Republic','Somalia','Comoros','Djibouti']

colors = ['blue','gray','red','green','blue',
          'steelblue','yellow','magenta','brown',
          'orange','tan','seagreen','olive',
          'turquoise','mintcream','yellowgreen',
          'darkkhaki','coral','chocolate','rosybrown',
          'dodgerblue','heather']

# We have data from the year 1961 to 2018
years = [1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971,
       1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982,
       1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993,
       1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004,
       2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
       2016, 2017, 2018]

def graph_1():
    region=[]
    for country in arab_countries:
        region.append(arab_df[arab_df.country.isin([country])]["UNRegion"].unique()[0])
    #     sub_region.append(arab_df[arab_df.country.isin([country])]["UN_subregion"].unique()[0])

    # There are 11 arab countries in Asia and 10 in Africa
    # region_labels holds the values of the regions
    # region_values holds values of the count of how many countries are there in that region
    region_labels = pd.Series(region).value_counts().index
    region_values = pd.Series(region).value_counts().values


    trace0  = go.Bar(x= region_labels,
                    y= region_values,
                    marker=dict(color='#85C1E9',
                                line=dict(color='rgb(174, 214, 241)',
                                        width=0.5,)),
                    opacity=0.5,
                    name = 'region',
                    hoverinfo="x + y")
    go_plot = [trace0]
    layout = go.Layout(
        title='Arab countries distrbutions according to UN regions',)
    fig = go.Figure(data=go_plot, layout=layout)
    return [go_plot, layout]
    # py.iplot(fig)


tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

#------------------------------------------------------------------------------------------#
#-------------------------------------------DASH-------------------------------------------#
#------------------------------------------------------------------------------------------#
layout = html.Div(
    children=[
        html.H1(children="Biocapacity and EF Analysis"),
        html.P(
            children=(
                "Analyze the behavior of avocado prices and the number"
                " of avocados sold in the US between 2015 and 2018"
            ),
        ),
        dcc.Tabs(id="tabs-example-graph", value='notab-content', children=[
        dcc.Tab(label='Basic Charts', value='tab-1', style = tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Population Visualizations', value='tab-2', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='GDP Visualizations', value='tab-3', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Footprint and Biocapacity', value='tab-4', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Others', value='tab-5')
        ], style=tabs_styles),
        dcc.Graph(
            figure={
                "data": graph_1()[0],
                "layout": graph_1()[1]
            },
        )
    ]
)
