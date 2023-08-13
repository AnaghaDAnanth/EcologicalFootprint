import pandas as pd
import math
from plotly import tools
import numpy as np
import plotly.graph_objs as go
import plotly.offline as py
import helperfunc as hlp


filepath = 'CountriesOnly.csv'

df = pd.read_csv(filepath, encoding = 'unicode_escape')
df = df.drop(['Unnamed: 0'], axis = 1)
df

# -------------------------Var Defns-------------------------#
lon = [-3.5673, -0.118092, 13.404954 ]
countries_map = ['Armenia', 'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Australia', 'Austria','Bahamas', 'Bahrain', 'Barbados', 'Bangladesh', 'Bermuda','Bhutan', 'Bolivia', 'Botswana', 'Brazil', 'Aruba', 'Belize','Brunei Darussalam', 'Bulgaria', 'Myanmar', 'Burundi', 'Cameroon','Canada', 'Cabo Verde', 'Cayman Islands', 'Central African Republic', 'Sri Lanka', 'Chad', 'Chile','Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica','Cuba', 'Cyprus', 'Czechoslovakia', 'Azerbaijan', 'Benin','Denmark', 'Dominica', 'Dominican Republic', 'Belarus', 'Ecuador','Egypt', 'El Salvador', 'Equatorial Guinea', 'Ethiopia PDR','Estonia', 'Fiji', 'Finland', 'France', 'French Guiana','French Polynesia', 'Djibouti', 'Georgia', 'Gabon', 'Gambia','Germany', 'Bosnia and Herzegovina', 'Ghana', 'Kiribati', 'Greece','Grenada', 'Guadeloupe', 'Guatemala', 'Guinea', 'Guyana', 'Haiti','Honduras', 'Hungary', 'Croatia', 'India', 'Indonesia','Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Kazakhstan', 'Jamaica', 'Japan', 'Jordan','Kyrgyzstan', 'Kenya', 'Cambodia',"Korea, Democratic People's Republic of", 'Korea, Republic of','Kuwait', 'Latvia', "Lao People's Democratic Republic", 'Lebanon','Lesotho', 'Liberia', 'Libyan Arab Jamahiriya', 'Lithuania','Madagascar', 'Malawi', 'Malaysia', 'Mali', 'Malta', 'Martinique','Mauritania', 'Mauritius', 'Mexico', 'Mongolia', 'Montserrat','Morocco', 'Mozambique', 'Micronesia, Federated States of','Moldova', 'Namibia', 'Nepal', 'Netherlands', 'Macedonia TFYR','Vanuatu', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria','Norway', 'Pakistan', 'Panama', 'Czech Republic','Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland','Portugal', 'Guinea-Bissau', 'Timor-Leste', 'Eritrea', 'Qatar','Zimbabwe', 'RÃ\x83Â©union', 'Romania', 'Rwanda', 'Russian Federation', 'Serbia and Montenegro', 'Saint Lucia','Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Sierra Leone','Slovenia', 'Slovakia', 'Singapore', 'Somalia','South Africa','Spain', 'Sudan (former)', 'Suriname', 'Tajikistan', 'Swaziland','Sweden', 'Switzerland', 'Syrian Arab Republic', 'Turkmenistan','Tanzania, United Republic of', 'Thailand', 'Togo', 'Tonga','Trinidad and Tobago', 'Oman', 'Tunisia', 'Turkey','United Arab Emirates', 'Uganda', 'USSR', 'United Kingdom','Ukraine', 'United States of America', 'Burkina Faso', 'Uruguay','Uzbekistan', 'Venezuela, Bolivarian Republic of', 'Viet Nam','Ethiopia', 'Samoa', 'Yugoslav SFR', 'Yemen','Congo, Democratic Republic of', 'Zambia', 'Belgium', 'Luxembourg','Serbia', 'Montenegro', 'Sudan', 'South Sudan', 'China','Solomon Islands', "CÃ´te d'Ivoire", 'Republic of Moldova','Republic of North Macedonia', 'Eswatini','State of Palestine', 'Saint Vincent and Grenadines']


arab_df = pd.read_csv("Asia.csv")
arab_countries = ['Sri Lanka','Saudi Arabia','Oman','Nepal','Yemen','Cambodia','Thailand','Kuwait','Malaysia','Mongolia','Bhutan','Philippines','Iraq','Georgia','Afghanistan','Cyprus',"Lao People's Democratic Republic",'Azerbaijan','Lebanon','Armenia','Timor-Leste','Tajikistan','Bahrain','Uzbekistan','Viet Nam','Korea, Republic of','United Arab Emirates','Kyrgyzstan','Bangladesh','Israel','Japan','Qatar','Syrian Arab Republic','Kazakhstan',
'Turkey','Indonesia','Singapore','India','Brunei Darussalam','Iran, Islamic Republic of','China','Jordan','Turkmenistan','Pakistan','Myanmar',"Korea, Democratic People's Republic of"]

colors = ['blue','gray','red','green','blue','steelblue','yellow','magenta','brown','orange','tan','seagreen','olive',
          'turquoise','mintcream','yellowgreen','darkkhaki','coral','chocolate','rosybrown','dodgerblue','heather']

# We have data from the year 1961 to 2018
years = [1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971,1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982,1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993,1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004,2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,2016, 2017, 2018]


difference  = []
countries_list = []
deficit_or_reserve = []
# Foreach arab country, find if it is deficit or reserve
for country in arab_countries:
    BiocapPerCap=np.array(hlp.extract_countries_feature_by_year(arab_df,[country],'total',2014)[0])
    EFConsPerCap=np.array(hlp.extract_countries_feature_by_year(arab_df,[country],'total',2014,record="EFConsPerCap")[0])
    difference_value = BiocapPerCap - EFConsPerCap
    if difference_value < 0 :
        deficit_or_reserve.append ("deficit")
        difference.append(np.abs(difference_value[0]))
    if difference_value > 0 :
        deficit_or_reserve.append("reserve")
        difference.append(difference_value[0])
    if difference_value.size==0:
        deficit_or_reserve.append("nan")
        difference.append(np.NAN)
    countries_list.append(country)
defict_reserve_df = pd.DataFrame({"country":countries_list,"deficit/reserve":deficit_or_reserve,"value":difference}).dropna().sort_values(by="value",ascending=False)



# Population analysis for 2000 and 2010
# Population analysis for 2000 and 2010
population_2000,available_countries_2000,excluded_countries_2000 = hlp.extract_countries_feature_by_year(arab_df,arab_countries,'population',2000)
population_2010,available_countries_2010,excluded_countries_2010 = hlp.extract_countries_feature_by_year(arab_df,arab_countries,'population',2010)


population_growth_rate = []
# For each country, finding growth rate of population in 10 years from 2000 to 2010
for i in range (0,len(population_2000)):
    growth_rate = np.round(hlp.calculate_growth_rate(population_2010[i],population_2000[i],10),2)
    population_growth_rate.append(growth_rate)
    
# available_countries = list(set(available_countries_2000).intersection(available_countries_2010))

growth_rate_df = pd.DataFrame({"country":available_countries_2000,"growth rate":population_growth_rate}).sort_values(by="growth rate",ascending=False)
hlp.print_excluded_countries(excluded_countries_2000, 2000)  
hlp.print_excluded_countries(excluded_countries_2010, 2010)


def extract_defict_value (df, country_name):
    # If country is deficit
    c = df[df.country.isin([country_name])]
    if c['deficit/reserve'].values.size != 0 :
        if (c['deficit/reserve'].values[0]=='deficit'):
            return c['value'].values[0]
        
countries = hlp.extract_countries_feature_by_year(arab_df,arab_countries,'GDP',2014)[1]
if 'Mauritania' in countries:
    countries.remove('Mauritania')     # remove Mauritania as it has no deficit 
        
deficit_value = []
for c in countries :
    if extract_defict_value(defict_reserve_df, c) != None:
        deficit_value.append(extract_defict_value(defict_reserve_df,c))
    else:
        continue

#````````````````````````````````````````````````````````````````````````````````````````````````````
Arab_BiocapTotal = []
Arab_EFConsTotal = []
Arab_BiocapPerCap = []
Arab_EFConsPerCap = []
world_BiocapTotal = []
world_EFConsTotal = []
mean_BiocapPerCap = []
mean_EFConsPerCap = []
for year in years :
    sum_BiocapTotal_value = np.array(hlp.extract_countries_feature_by_year(arab_df,arab_countries,'total',year,record= 'BiocapTotGHA')[0]).sum()
    sum_EFConsTotal_value = np.array(hlp.extract_countries_feature_by_year(arab_df,arab_countries,'total',year,record='EFConsTotGHA')[0]).sum()
    sum_population_per_year = np.array(hlp.extract_countries_feature_by_year(arab_df,arab_countries,'population',year)[0]).sum()
    world_BiocapTotal.append(np.array(hlp.extract_countries_feature_by_year(df,['World'],'total',year,record= 'BiocapTotGHA')[0]))
    world_EFConsTotal.append(np.array(hlp.extract_countries_feature_by_year(df,['World'],'total',year,record= 'EFConsTotGHA')[0]))
    Arab_BiocapTotal.append(sum_BiocapTotal_value)
    Arab_EFConsTotal.append(sum_EFConsTotal_value)
    Arab_BiocapPerCap.append(sum_BiocapTotal_value/sum_population_per_year)
    Arab_EFConsPerCap.append(sum_EFConsTotal_value/sum_population_per_year)
    mean_BiocapPerCap.append(np.array(hlp.extract_countries_feature_by_year(arab_df,arab_countries,'total',year)[0]).mean())
    mean_EFConsPerCap.append(np.array(hlp.extract_countries_feature_by_year(arab_df,arab_countries,'total',year,record='EFConsPerCap')[0]).mean())
# print("--------------------------")
# print(world_BiocapTotal, world_EFConsTotal)


import datetime
arab_eod_dates = []
eod_dates_world=[]

def calc_earth_overshot_day(biocap,ecofootp):
    eod = (np.array(biocap) / np.array(ecofootp))*365
    return eod

eod_arab = calc_earth_overshot_day(Arab_BiocapTotal,Arab_EFConsTotal)
eod_world = calc_earth_overshot_day(world_BiocapTotal,world_EFConsTotal)

eod_month_arab = []
eod_month_world = []

for i in range (0,len(eod_arab)):
    if eod_arab[i]>365:
        arab_eod_dates.append("no EOD")
        eod_month_arab.append("no EOD")
    if eod_world[i]>365:
        eod_dates_world.append("no EOD")
        eod_month_world.append("no EOD")
    if eod_arab[i] < 365:
        date_arab = datetime.datetime(years[i],1,1) + datetime.timedelta(days=eod_arab[i])
        eod_month_arab.append(date_arab.strftime('%b'))
        arab_eod_dates.append(date_arab.strftime('%b-%d'))
    if eod_world[i] < 365:
        date_world = datetime.datetime(years[i],1,1) + datetime.timedelta(days=int(eod_world[i]))
        eod_month_world.append(date_world.strftime('%b'))
        eod_dates_world.append(date_world.strftime('%b-%d'))
        #[19:] represents the year that the EOD begins to appear 

eod_df = pd.DataFrame({"year":years[19:],"Arab Earth Overshoot Day":arab_eod_dates[19:],"World Earth Overshoot Day":eod_dates_world[19:]})


#------------------------ T1 ------------------------#
#------------------------ T1 ------------------------#
def world_map():
    trace0 = go.Scattergeo(marker = dict(color='#D4FF76', size=7, line=dict(color = 'white',width = 0.5)), locations = countries_map, locationmode = 'country names')
    go_plot = [trace0]

    fig = go.Figure(data=go_plot)
    fig = fig.update_geos(projection_type="orthographic")
    fig = fig.update_layout(height=500)
    fig = fig.update_geos(showocean=True, coastlinecolor="#DCF7DD",framecolor="#D6EAF8", lakecolor="#4FA1C2", landcolor="#7AC67B", oceancolor="#48B7DD")
    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20),)
    lon_range = np.arange(-180, 180, 2)
    frames = [go.Frame(layout=dict(geo_center_lon=lon,
                                geo_projection_rotation_lon =lon
                            )) for lon in lon_range]
    fig.update(frames=frames)
    return fig
   
#------------------------ Region Chart ------------------------#
def graph_1(arab_countries):
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


def graph_2(arab_countries):
    countries = hlp.extract_countries_feature_by_year(arab_df,arab_countries,'GDP',2014)[1]
    y = hlp.extract_countries_feature_by_year(arab_df,countries,'GDP',2014)[0]
    x = hlp.extract_countries_feature_by_year(arab_df,countries,'population',2014)[0]

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



#------------------------ T2 ------------------------#
#------------------------ T2 ------------------------#
def graph_3(arab_countries):
    population, available_countries, excluded_countries = hlp.extract_countries_feature_by_year(arab_df,arab_countries,'population',2014)

    # Manually adding population for Sudan
    available_countries.append("Sudan")
    population.append(37737900)


    population_df = pd.DataFrame({'country':available_countries,'population':population}).sort_values(by='population',ascending=True) 
    population_list = list (population_df['population'])
    countries = list (population_df['country'])
    annotations = []
    y_nw = np.array(population_list)

    for ydn,  xd in zip(y_nw, countries):
        # labeling the scatter savings
        annotations.append(dict(xref='x', yref='y',
                                y=xd, x=ydn + 5000000,
                                text='{:,} M'.format(np.round(ydn/10**6,2)),
                                font=dict(family='Arial', size=12,
                                        color='rgb(50, 0, 50)'),
                                showarrow=False))
    fig  = {
    "data": [
        {
        "values": population_list,
        "labels": countries,
        "hoverinfo":"label+percent",
        "hole": .3,
        "type": "pie",
        'domain': {'x': [.4, 1],
                        'y': [0.2, .8]},
                'hoverinfo':'label+percent',
                'textinfo':'percent'
        },
        {
            "x": population_list,
            "y": countries,
            "type": "bar",
            "orientation" :'h',
            "hoverinfo":"x",
            "marker" : dict(color='rgba(214, 234, 248,0.7)',
                            line=dict(color='rgb(174, 214, 241)',
                                        width=2)),
            
            "opacity":0.7,
            "name":"Population",
            } 
    ],
    "layout": {
            "title":"Arab Countries Population Analysis",
            'annotations': annotations,
            "yaxis":dict(
                showgrid=False,
                showline=False,
                showticklabels=True,
                tickfont=dict(family='Arial', size=12,color='rgb(50, 0, 50)')),
            "width": 1000,
            "height":700,
        "paper_bgcolor":'rgb(248, 248, 248)',
        "plot_bgcolor":'rgb(240, 245, 255)',
        
    }}
    # v = py.iplot(fig)
    return [fig["data"], fig["layout"]]

def graph_4(arab_countries):
    traces = []
    # For each arab country, append the info to a trace
    for i in range(len(arab_countries)):
        country_by_record = hlp.extract_country_by_record(arab_df,arab_countries[i],'BiocapPerCap')
        traces.append(go.Scatter(
                x=country_by_record['year'],
                y=country_by_record['population'],
                mode='lines',
                line=dict(color=colors[i], width=1.5),
                text= arab_countries[i],
                hoverinfo="text + x + y",
                connectgaps=True,
                name =arab_countries[i],
                textfont=dict(family='Arial', size=12),
        ))

    layout = go.Layout(
        title = "Arab Countries Population Growth Analysis",
        xaxis=dict(
                showline=True,
                showgrid=True,
                showticklabels=True,
                linecolor='rgb(150, 150, 150)',
                linewidth=2,
                gridcolor='rgb(174, 214, 241)',
                ticks='outside',
                tickcolor='rgb(80, 80, 80)',
                tickwidth=2,
                ticklen=5,
                tickfont=dict(
                family='Arial',
                size=13,
                color='rgb(23, 32, 42)',
            ),
        ),
        yaxis=dict(
                showgrid=True,
                zeroline=True,
                showline=False,
                gridcolor='rgb(174, 214, 241)',
                showticklabels=True,
                tickcolor='rgb(150, 150, 150)',
                tickwidth=2,
                ticklen=5,
                tickfont=dict(
                family='Arial',
                size=13,
                color='rgb(23, 32, 42)')
        ),
        font=dict(family='Arial', size=12,
                color='rgb(23, 32, 42)'),
                showlegend=True, 
                width = 900,
                height = 700,
                paper_bgcolor='rgb(248, 248, 248)',
                plot_bgcolor='rgb(240, 245, 255)'
    )
    return [traces, layout]

def graph_5():
    table = go.Table(header=dict(values=['Country', 'Growth rate']),
                cells=dict(values= [growth_rate_df['country'],growth_rate_df['growth rate'].astype(str)+"%"]))
        
    fig = go.Figure(data=[table])
    return [[table]]

def graph_6():
    GDP,available_countries, excluded_countries = hlp.extract_countries_feature_by_year(arab_df,arab_countries,'GDP',2014)
    growth_rate_df = pd.DataFrame({"country":available_countries,"growth rate":population_growth_rate}).sort_values(by="growth rate",ascending=False)
    growth_rate_df =growth_rate_df.sort_values(by="growth rate",ascending=True)
    trace0  = go.Bar(x= growth_rate_df["growth rate"],
                        y= growth_rate_df["country"],
                        orientation ='h',
                        marker=dict(color='rgba(214, 234, 248,0.7)',
                                    line=dict(color='rgb(174, 214, 241)',
                                            width=2)),
                    opacity=0.7,
                    hoverinfo="x + y")

    annotations = []
    y_nw = np.array(growth_rate_df["growth rate"])
    for ydn,  xd in zip(y_nw, growth_rate_df["country"]):
        # labeling the scatter savings
        annotations.append(dict(xref='x', yref='y',
                                y=xd, x=ydn+0.9,
                                text='{:,} %'.format(np.round(ydn,2)),
                                font=dict(family='Arial', size=12,
                                            color='rgba(23, 32, 42, 1.0)'),
                                showarrow=False))
    layout = go.Layout(
                    title='Arab Countries Annual Growth Rate of Population',
                    margin=dict(
                            l=130,
                            r=20,
                            t=30,
                            b=30,
                        ),
                    annotations = annotations,
                    xaxis=dict(showgrid=True,
                            gridcolor="rgba(36, 113, 163, .15)",
                            showticklabels=True,
                            tickfont=dict(family='Arial', size=12,color='rgb(23, 32, 42)')),
                    yaxis=dict(showgrid=False,
                            showline=False,
                            linecolor='rgba(250, 80, 0, 1.0)',
                            showticklabels=True,
                            tickfont=dict(family='Arial', size=12,color='rgb(23, 32, 42)')),
                    font=dict(family='Arial', size=12,
                            color='rgb(23, 32, 42)'),
                    width = 1000,
                    height = 600,
                    paper_bgcolor='rgb(248, 248, 248)',
                    plot_bgcolor='rgb(240, 245, 255)',
                    )
    # fig = go.Figure(data=[trace0], layout=layout)
    return [[trace0], layout]

def graph_7():
    arab_countries_population = []
    for year in years:
        sum_population_per_year = np.array(hlp.extract_countries_feature_by_year(arab_df,arab_countries,'population',year)[0]).sum()
        arab_countries_population.append(sum_population_per_year)
    arab_population_growth_rate = hlp.calculate_growth_rate(arab_countries_population[49],arab_countries_population[24],25)
    trace0 = go.Scatter(
        x= years[24:49],
        y= arab_countries_population[24:49],
        hoverinfo = 'name+x+y',
        name='Population',
        mode = "lines",
        line=dict(
            color='rgb(174, 214, 241)',
            width= 3))
    layout = go.Layout(
        title = "Total Population Growth",
        annotations = [dict(xref = 'x', yref = 'y',
                            x = 1990, y = arab_countries_population[45],
                            text='growth rate = {0} %'.format(np.round(arab_population_growth_rate,2)),
                            font=dict(family='Arial', size=20,
                                    color='rgba(31, 97, 141, 1.0)'),
                            showarrow=False)],
        xaxis=dict(
            showline=False,
            showgrid=True,
            showticklabels=True,
            linecolor='rgb(150, 150, 150)',
            linewidth=2,
            gridcolor='rgb(174, 214, 241)',
            ticks='outside',
            tickcolor='rgb(80, 80, 80)',
            tickwidth=2,
            ticklen=5,
            tickfont=dict(
                family='Arial',
                size=13,
                color='rgb(23, 32, 42)',
            ),
        ),
        yaxis=dict(
            showgrid=True,
            zeroline=True,
            showline=False,
            gridcolor='rgb(174, 214, 241)',
            showticklabels=True,
            tickcolor='rgb(180, 180, 180)',
            tickwidth=2,
            ticklen=5,
            tickfont=dict(
                family='Arial',
                size=13,
                color='rgb(23, 32, 42)')
        ),
        font=dict(family='Arial', size=12,
                    color='rgb(23, 32, 42)'),
        showlegend=True, 
        width = 900,
        height = 700,
        paper_bgcolor='rgb(248, 248, 248)',
        plot_bgcolor='rgb(240, 245, 255)',)
    return [[trace0], layout]


#------------------------ T3 ------------------------#
#------------------------ T3 ------------------------#
def graph_8(arab_countries):
    traces = []
    annotations = []
    for i in range(len(arab_countries)):
        country_by_record = hlp.extract_country_by_record(arab_df,arab_countries[i],'BiocapPerCap')
        traces.append(go.Scatter(
            x=country_by_record['year'],
            y=country_by_record['GDP'],
            mode='lines',
            line=dict(color=colors[i], width=1.5),
            text= arab_countries[i]+"<br>"+ country_by_record['GDP'].dropna().apply(lambda x:int(x)).astype(str)+" $",
            hoverinfo="text + x ",
            connectgaps=True,
            name =arab_countries[i],
            textfont=dict(family='Arial', size=12),
        ))

    world_by_record = hlp.extract_country_by_record(df,'World','BiocapPerCap')
    traces.append(go.Scatter(
            x=world_by_record['year'],
            y=world_by_record['GDP'],
            mode='lines',
            line=dict(color="rgb(255,0,0)", width=2.5, dash = 'dash'),
            text= "World"+"<br>"+ world_by_record['GDP'].dropna().apply(lambda x:int(x)).astype(str)+" $",
            hoverinfo="text + x ",
            connectgaps=True,
            name ="World",
            textfont=dict(family='Arial', size=12),
        ))

    layout = go.Layout(
        title = "Arab countries GDP per capita",
        xaxis=dict(
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='rgb(150, 150, 150)',
            linewidth=2,
            gridcolor='rgb(253, 254, 254)',
            ticks='outside',
            tickcolor='rgb(80, 80, 80)',
            tickwidth=2,
            ticklen=5,
            tickfont=dict(
                family='Arial',
                size=13,
                color='rgb(23, 32, 42)',
            ),
        ),
        yaxis=dict(
            showgrid=True,
            zeroline=True,
            showline=False,
            gridcolor='rgb(253, 254, 254)',
            showticklabels=True,
            tickcolor='rgb(150, 150, 150)',
            tickwidth=2,
            ticklen=5,
            tickfont=dict(
                family='Arial',
                size=13,
                color='rgb(23, 32, 42)')
        ),
        font=dict(family='Arial', size=12,
                    color='rgb(23, 32, 42)'),
        showlegend=True, 
        width = 900,
        height = 700,
        paper_bgcolor='rgb(248, 248, 248)',
        plot_bgcolor='rgb(240, 245, 255)',
    )
    return [traces, layout]

def graph_9():
    GDP,available_countries, excluded_countries = hlp.extract_countries_feature_by_year(arab_df,arab_countries,'GDP',2014)
    GDP_df = pd.DataFrame({'country':available_countries,'GDP':GDP}).sort_values(by='GDP',ascending=True)
    trace0  = go.Bar(x= GDP_df["GDP"],
                        y= GDP_df["country"],
                        orientation ='h',
                        marker=dict(color='rgba(214, 234, 248,0.7)',
                                    line=dict(color='rgb(174, 214, 241)',
                                            width=2)),
                        opacity=0.7,
                        name="GDP",
                    hoverinfo="name+x + y")

    annotations = []
    y_nw = np.array(GDP_df["GDP"])
    for ydn,  xd in zip(y_nw, GDP_df["country"]):
        # labeling the scatter savings
        annotations.append(dict(xref='x', yref='y',
                                y=xd, x=ydn+3000,
                                text='{:,} $'.format(np.int(ydn)),
                                font=dict(family='Arial', size=12,
                                            color='rgba(23, 32, 42, 1.0)'),
                                showarrow=False))

    layout = go.Layout(
        title='2014 Arab countries GDP per Capita',
            margin=dict(
            l=130,
            r=20,
            t=30,
            b=30,
        ),
        annotations = annotations,
        xaxis=dict(showgrid=True,
                    gridcolor="rgba(36, 113, 163, .15)",
                    showticklabels=True,
                    tickfont=dict(family='Arial', size=12,color='rgba(23, 32, 42, 1.0)')),
        yaxis=dict(showgrid=False,
                    showline=False,
                    linecolor='rgba(250, 80, 0, 1.0)',
                    showticklabels=True,
                    tickfont=dict(family='Arial', size=12,color='rgba(23, 32, 42, 1.0)')),
        font=dict(family='Raleway', size=12,
                                            color='rgba(50, 50, 50, 1.0)'),
        width = 1000,
        height = 600,
        paper_bgcolor='rgb(248, 248, 248)',
        plot_bgcolor='rgb(240, 245, 255)',
                    )
    return [[trace0], layout]


#------------------------ T4 ------------------------#
#------------------------ T4 ------------------------#
def graph_10(arab_countries):
    record ={1:['BiocapPerCap','EFConsPerCap','rgba(0,255,0,1)','rgba(255,0,0,1)'],
             2:['BiocapTotGHA','EFConsTotGHA','rgba(0,140,0,1)','rgba(140,0,0,1)'],}
    # arab_countries = [arab_countries]
    for c in range (0,len(arab_countries)):
        fig = tools.make_subplots(rows=1, cols=2, specs=[[{},{}]], horizontal_spacing=0.1,
                                subplot_titles=["BioCapacity vs Ecological footprint (per capita)","BioCapacity vs Ecological footprint (GHA)"])
        for r in record.keys():
            country_by_record_bio = hlp.extract_country_by_record(arab_df,arab_countries[c],record[r][0])
            country_by_record_cons = hlp.extract_country_by_record(arab_df,arab_countries[c],record[r][1])
            trace1 = go.Scatter(x=country_by_record_bio['year'], y=country_by_record_bio['total'],
            mode= 'lines',
            name = record[r][0],
            line=dict(color=record[r][2], width=1.5),
            hoverinfo="y + x ",
            textfont=dict(family='Arial', size=12),
        )
            trace2 = go.Scatter(
            x=country_by_record_cons['year'],
            y=country_by_record_cons['total'],
            mode='lines',
            name = record[r][1],
            line=dict(color=record[r][3], width=1.5),
            hoverinfo="y + x ",
            textfont=dict(family='Arial', size=12),
        )
            data= [trace1,trace2]

            fig.append_trace(trace1, 1, r)
            fig.append_trace(trace2, 1, r)
        fig['layout'].update(height=450, width=1100,title=arab_countries[c])
    return fig

def graph_11(arab_countries):
    Arab_BiocapTotal = []
    Arab_EFConsTotal = []
    Arab_BiocapPerCap = []
    Arab_EFConsPerCap = []
    world_BiocapTotal = []
    world_EFConsTotal = []
    mean_BiocapPerCap = []
    mean_EFConsPerCap = []
    for year in years :
        sum_BiocapTotal_value = np.array(hlp.extract_countries_feature_by_year(arab_df,arab_countries,'total',year,record= 'BiocapTotGHA')[0]).sum()
        sum_EFConsTotal_value = np.array(hlp.extract_countries_feature_by_year(arab_df,arab_countries,'total',year,record='EFConsTotGHA')[0]).sum()
        sum_population_per_year = np.array(hlp.extract_countries_feature_by_year(arab_df,arab_countries,'population',year)[0]).sum()
        world_BiocapTotal.append(np.array(hlp.extract_countries_feature_by_year(df,['World'],'total',year,record= 'BiocapTotGHA')[0]))
        world_EFConsTotal.append(np.array(hlp.extract_countries_feature_by_year(df,['World'],'total',year,record= 'EFConsTotGHA')[0]))
        Arab_BiocapTotal.append(sum_BiocapTotal_value)
        Arab_EFConsTotal.append(sum_EFConsTotal_value)
        Arab_BiocapPerCap.append(sum_BiocapTotal_value/sum_population_per_year)
        Arab_EFConsPerCap.append(sum_EFConsTotal_value/sum_population_per_year)
        mean_BiocapPerCap.append(np.array(hlp.extract_countries_feature_by_year(arab_df,arab_countries,'total',year)[0]).mean())
        mean_EFConsPerCap.append(np.array(hlp.extract_countries_feature_by_year(arab_df,arab_countries,'total',year,record='EFConsPerCap')[0]).mean())

    fig = tools.make_subplots(rows=2, cols=2, specs=[[{},{}],[{'colspan': 2}, None]], horizontal_spacing=0.1, vertical_spacing = 0.1,
                         subplot_titles=["Per capita","Mean (per capita)","Total (GHA)"])
    arab_biocapPerCap_plt = go.Scatter(
                x=years[19:],
                y=Arab_BiocapPerCap[19:],
                mode= 'lines',
                name = "Biocapcity",
                line=dict(color="green", width=1.5),
                hoverinfo="y + x ",
                textfont=dict(family='Arial', size=12),
            )
    arab_EFperCap_plt = go.Scatter(
                x=years[19:],
                y=Arab_EFConsPerCap[19:],
                mode='lines',
                name = "Ecological footprint",
                line=dict(color="red", width=1.5),
                hoverinfo="y + x ",
                textfont=dict(family='Arial', size=12),
            )

    fig.append_trace(arab_biocapPerCap_plt, 1, 1)
    fig.append_trace(arab_EFperCap_plt, 1, 1)

    arab_meanBiocapPerCap_plt = go.Scatter(
                x=years[19:],
                y=mean_BiocapPerCap[19:],
                mode= 'lines',
                showlegend = False,
                line=dict(color="green", width=1.5),
                hoverinfo="y + x ",
                textfont=dict(family='Arial', size=12),
            )
    arab_meanEFperCap_plt = go.Scatter(
                x=years[19:],
                y=mean_EFConsPerCap[19:],
                mode='lines',
                showlegend = False,
                line=dict(color="red", width=1.5),
                hoverinfo="y + x ",
                textfont=dict(family='Arial', size=12),
            )

    fig.append_trace(arab_meanBiocapPerCap_plt, 1, 2)
    fig.append_trace(arab_meanEFperCap_plt, 1, 2)

    arab_totalBiocap_plt = go.Scatter(
                x=years[19:],
                y=Arab_BiocapTotal[19:],
                mode= 'lines',
                showlegend = False,
                line=dict(color="green", width=1.5),
                hoverinfo="y + x ",
                textfont=dict(family='Arial', size=12),
            )
    arab_totalEF_plt = go.Scatter(
                x=years[19:],
                y=Arab_EFConsTotal[19:],
                mode='lines',
                showlegend = False,
                line=dict(color="red", width=1.5),
                hoverinfo="y + x ",
                textfont=dict(family='Arial', size=12),
            )

    fig.append_trace(arab_totalBiocap_plt, 2, 1)
    fig.append_trace(arab_totalEF_plt, 2, 1)

    fig['layout'].update(height=900, width=1000,
                            title= "Arab World BioCapacity vs Ecological footprint")
    return fig


def graph_12(arab_countries):
    difference  = []
    countries_list = []
    deficit_or_reserve = []

    # Foreach arab country, find if it is deficit or reserve
    for country in arab_countries:
        BiocapPerCap=np.array(hlp.extract_countries_feature_by_year(arab_df,[country],'total',2014)[0])
        EFConsPerCap=np.array(hlp.extract_countries_feature_by_year(arab_df,[country],'total',2014,record="EFConsPerCap")[0])
        difference_value = BiocapPerCap - EFConsPerCap
        if difference_value < 0 :
            deficit_or_reserve.append ("deficit")
            difference.append(np.abs(difference_value[0]))
        if difference_value > 0 :
            deficit_or_reserve.append("reserve")
            difference.append(difference_value[0])
        if difference_value.size==0:
            deficit_or_reserve.append("nan")
            difference.append(np.NAN)
        countries_list.append(country)
        
    defict_reserve_df = pd.DataFrame({"country":countries_list,"deficit/reserve":deficit_or_reserve,"value":difference}).dropna().sort_values(by="value",ascending=False)
    trace0 = go.Bar(
    y=defict_reserve_df[defict_reserve_df['deficit/reserve'].isin(['deficit'])]['country'],
    x=defict_reserve_df[defict_reserve_df['deficit/reserve'].isin(['deficit'])]['value'],
    orientation ='h',
    name='Deficit',
    marker=dict(
        color='rgb(245, 183, 177)',line=dict(color='rgb(241, 148, 138)',
                                        width=2)
    )
)
    trace1 = go.Bar(
        y=defict_reserve_df[defict_reserve_df['deficit/reserve'].isin(['reserve'])]['country'],
        x=defict_reserve_df[defict_reserve_df['deficit/reserve'].isin(['reserve'])]['value'],
        orientation ='h',
        name='Reserve',
        marker=dict(
            color='rgb(171, 235, 198)',line=dict(color='rgb(130, 224, 170)',
                                            width=2)
        )
    )
    data = [trace0, trace1]
    layout = go.Layout(title = "Arab countries Ecological footprint [Deficit/Reserve] (per capita)",
                        yaxis = dict(showline = False,
                                    zeroline = False),
                        width=900,height=500,
                        margin=dict(
                            l=140,
                            r=20,
                            t=30,
                            b=30)
                        )
    fig = go.Figure(data=data, layout=layout)
    return fig
# print(graph_10(arab_countries))

def graph_13(arab_countries):
    countries = hlp.extract_countries_feature_by_year(arab_df,arab_countries,'GDP',2014)[1]
    if 'Mauritania' in countries:
        countries.remove('Mauritania')     # remove Mauritania as it has no deficit 
    x = hlp.extract_countries_feature_by_year(arab_df,countries,'GDP',2014)[0]
    y = deficit_value
    colors = np.random.rand(100)
    sz = (np.array(y)*10000)
    text = []
    for i in range (len(countries)):
        text.append(countries[i]+"<br>"+"GDP: {0} K".format(np.round((x[i]/10**3),2))+"<br>"+"Deficit: {0}".format(np.round((y[i]),2)))

    annotations = []
    y_nw = np.array(y)
    for ydn,  xd , c in zip(y_nw, x,countries):
        # labeling the scatter savings
        annotations.append(dict(xref='x', yref='y',
                                y=ydn, x=xd,
                                text= c,
                                font=dict(family='Raleway', size=11,
                                            color='rgba(50, 50, 50, 1.0)'),
                                showarrow=False))
    trace = go.Scatter(x=x,
                    y=y,
                    text = text,
                    mode='markers',
                    hoverinfo = 'text ',
                    marker={'size': sz,
                            'color': colors,
                            'opacity': 0.5,
                            'sizemode' : 'area',
                            'sizeref' : 80,
                            'colorscale': 'Viridis'
                            });
    layout = go.Layout(title= " Ecological Deficit and GDP",
                        yaxis=dict(title = "Ecological deficit (per capita)"),
                        xaxis=dict(title = "GDP per capita"),
                        annotations = annotations,
                        height = 700,
                        width = 1500)
    fig = go.Figure(data=[trace],layout = layout)
    return [[trace], layout]


def graph_14():
    Arab_BiocapTotal = []
    Arab_EFConsTotal = []
    Arab_BiocapPerCap = []
    Arab_EFConsPerCap = []
    world_BiocapTotal = []
    world_EFConsTotal = []
    mean_BiocapPerCap = []
    mean_EFConsPerCap = []
    for year in years :
        sum_BiocapTotal_value = np.array(hlp.extract_countries_feature_by_year(arab_df,arab_countries,'total',year,record= 'BiocapTotGHA')[0]).sum()
        sum_EFConsTotal_value = np.array(hlp.extract_countries_feature_by_year(arab_df,arab_countries,'total',year,record='EFConsTotGHA')[0]).sum()
        sum_population_per_year = np.array(hlp.extract_countries_feature_by_year(arab_df,arab_countries,'population',year)[0]).sum()
        world_BiocapTotal.append(np.array(hlp.extract_countries_feature_by_year(arab_df,['World'],'total',year,record= 'BiocapTotGHA')[0]))
        world_EFConsTotal.append(np.array(hlp.extract_countries_feature_by_year(arab_df,['World'],'total',year,record= 'EFConsTotGHA')[0]))
        Arab_BiocapTotal.append(sum_BiocapTotal_value)
        Arab_EFConsTotal.append(sum_EFConsTotal_value)
        Arab_BiocapPerCap.append(sum_BiocapTotal_value/sum_population_per_year)
        Arab_EFConsPerCap.append(sum_EFConsTotal_value/sum_population_per_year)
        mean_BiocapPerCap.append(np.array(hlp.extract_countries_feature_by_year(arab_df,arab_countries,'total',year)[0]).mean())
        mean_EFConsPerCap.append(np.array(hlp.extract_countries_feature_by_year(arab_df,arab_countries,'total',year,record='EFConsPerCap')[0]).mean())

    EOD_arab_plt = go.Scatter(
            x=eod_df['year'],
            y= eod_month_arab[19:],
            mode= 'lines',
            name = "Arab EOD",
            text = eod_df["Arab Earth Overshoot Day"],
            line=dict(color="green", width=1.5),
            hoverinfo="name + text + x ",
            textfont=dict(family='Arial', size=12),
        )
    EOD_world_plt = go.Scatter(
                x=eod_df['year'],
                y= eod_month_world[19:],
                mode= 'lines',
                name = "World EOD",
                text = eod_df["World Earth Overshoot Day"],
                line=dict(color="red", width=1.5),
                hoverinfo="name + text + x ",
                textfont=dict(family='Arial', size=12),
            )
    layout = go.Layout(title= "Earth Overshoot Day",
                        yaxis=dict(title = "Month"),
                        xaxis=dict(title = "Year"),
                        height = 500,
                        width = 800)

    return [[EOD_arab_plt,EOD_world_plt], layout]

def graph_15(arab_countries):
    Arab_carbon,available_countries,excluded_countries = hlp.extract_countries_feature_by_year(arab_df,arab_countries,'carbon',2014,record="EFConsPerCap")
    carbon_df = pd.DataFrame({'country':available_countries,'carbon':Arab_carbon}).sort_values(by='carbon',ascending=False)
    avail_countris = hlp.extract_countries_feature_by_year(arab_df,carbon_df['country'],'GDP',2014)[1]
    y = avail_countris
    x = hlp.extract_countries_feature_by_year(arab_df,avail_countris,'GDP',2014)[0]
    size = hlp.extract_countries_feature_by_year(arab_df,avail_countris,'carbon',2014,record="EFConsPerCap")[0]
    colors = size
    text = []
    for i in range (len(avail_countris)):
        text.append(y[i]+"<br>"+"GDP Percap: {0} K".format(np.round((x[i]/10**3),2))+"<br>"+"EFcarbon: {0} ".format(np.round((np.array(size)[i]),2)))

        trace = go.Scatter(x=x,
                        y=y,
                        text = text,
                        mode='markers',
                        hoverinfo = 'text ',
                        name = "EFCarbon",
                        showlegend = False,
                        marker={'size': size,        
                                'color': colors,
                                'opacity': 0.6,
                                'sizemode' : 'area',
                                'sizeref' : 0.005,
                                'colorscale': 'Portland',
                                    'showscale' : True,
                                    'cmax' : np.max(size),
                                    'cmin' : np.min(size),
                                    'colorbar' : dict( y= 0.52,
                                                    len= .8,
                                                    x = 1,
                                                    title = "EF Carbon",
                                                    titlefont = dict(size=15))
                                },

                            );
        layout = go.Layout(
                            title = "Ecological footprint of Carbon and GDP (per capita) [2014]",
                            xaxis=dict(title = "GDP (per capita)",
                                        titlefont = dict (family = "Arial"),
                                        zeroline=False),
                            yaxis=dict(
                                zeroline=True,
                                showticklabels=True,
                                tickfont=dict(family='Arial', size=12)),
                            margin=dict(
                                l=140,
                                r=20,
                                t=40,
                                b=45,),
                            width = 1000,
                            height = 700)
        fig = go.Figure(data=[trace],layout = layout)
    return [[trace], layout]