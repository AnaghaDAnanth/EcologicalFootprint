import pandas as pd
import math
import numpy as np
import plotly.graph_objs as go

arab_df = pd.read_csv("Arab.csv")
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

# Extracts the rows for a particular country for a particular record type for all 58 years
def extract_country_by_record(df, country_name, record):
    country_foot_print=df[df.country.isin([country_name])]
    country_by_record = country_foot_print [country_foot_print.record.isin([record])]
    return country_by_record

# Returns the following lists - 
# 1. feature_values -> list of population values
# 2. available_countries -> list of countries with population data
# 3. excluded_countries -> list of countries without population data
# feature_value has the value of the column for a particular year of that country
# example: can have value of Lebanon's population for year 2014
def extract_countries_feature_by_year(df,countries_list,feature,year,record="BiocapPerCap"):
    excluded_countries=[]
    feature_values=[]
    available_countries=[]
    # Looping through list of arab countries
    for i in range (0,len(countries_list)):
        country_by_record = extract_country_by_record(df,countries_list[i],record)
        feature_value = country_by_record.loc[lambda df1: country_by_record.year == year][feature].values
        if  feature_value.size==0 or math.isnan(feature_value[0]) :
            excluded_countries.append(countries_list[i])
        else:
            feature_values.append(feature_value[0]) 
            available_countries.append(countries_list[i])
            
#  Uncomment if you need to print the excluded countries in the year
#     if len(excluded_countries) != 0:
#         print("excluded countries in {0} are : ".format(year))
#         for i in excluded_countries:
#             print(i)
    return feature_values, available_countries, excluded_countries 


def print_excluded_countries (excluded_countries,year):
    if len(excluded_countries) != 0:
        print("excluded countries from dataset in {0} are : ".format(year))
        for i in excluded_countries:
            print(i)   
            
# Returns percentage_growth_rate
def calculate_growth_rate(present,past,period):
    #present : present year , past: past year , period: number of years between present and past
    percentage_growth_rate = ((present - past)/(past*period))*100
    return percentage_growth_rate



#------------------------ T1 ------------------------#
#------------------------ Region Chart ------------------------#
def graph_1():
    region=[]
    for country in arab_countries:
        region.append(arab_df[arab_df.country.isin([country])]["UNRegion"].unique()[0])
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


def graph_2():
    countries = extract_countries_feature_by_year(arab_df,arab_countries,'GDP',2014)[1]
    y = extract_countries_feature_by_year(arab_df,countries,'GDP',2014)[0]
    x = extract_countries_feature_by_year(arab_df,countries,'population',2014)[0]

    colors = np.random.rand(22)
    text = []
    for i in range (len(countries)):
        text.append(countries[i]+"<br>"+"GDP Percap: {0} K".format(np.round((y[i]/10**3),2))+"<br>"+"population: {0} M".format(np.round((x[i]/10**6),2)))
    annotations = []
    y_nw = np.array(y)
    for ydn,  xd , c in zip(y_nw, x,countries):
        # labeling the scatter savings
        annotations.append(dict(xref='x', yref='y',
                                y=ydn, x=xd,
                                text= c,
                                font=dict(family='Raleway', size=12,
                                            color='rgba(50, 50, 50, 1.0)'),
                                showarrow=False))
    # The marker size is proportional to population
    trace = go.Scatter(x=x,
                    y=y,
                    text = text,
                    mode='markers',
                    hoverinfo = 'text ',
                    marker={'size': x,        
                            'color': colors,
                            'opacity': 0.6,
                            'sizemode' : 'area',
                            'sizeref' : 40000,
                            'colorscale': 'Viridis'
                            });
    layout = go.Layout(title = " GDP and Population",
                        yaxis=dict(title = "GDP per capita"),
                        xaxis=dict(title = "Population"),
                        height = 700)
    fig = go.Figure(data=[trace],layout = layout)
    dat = [trace]
    return [dat, layout]
