import graphs_europe as graphs
from dash import html, dcc

#----------------------------Tab 1----------------------------#
def tab1GraphsFunctionCall(graphlist, countrylist):
    if graphlist == 'Region-wise distribution':
        # print("Reached")
        return dcc.Graph(id='display-map', 
                            figure={
                            "data": graphs.graph_1(countrylist)[0],
                            "layout": graphs.graph_1(countrylist)[1]
                        })
    else:
        return dcc.Graph(id='display-map', 
                            figure={
                            "data": graphs.graph_2(countrylist)[0],
                            "layout": graphs.graph_2(countrylist)[1]
                        })
    

#----------------------------Tab 2----------------------------#    
def tab2GraphsFunctionCall(graphlist, countrylist):
    if graphlist == 'Basic Population Analysis':
        # print("Reached")
        return dcc.Graph(id='display-map', 
                            figure={
                            "data": graphs.graph_3(countrylist)[0],
                            "layout": graphs.graph_3(countrylist)[1]
                        })
    elif graphlist == 'Population Growth Analysis':
        return dcc.Graph(id='display-map', 
                            figure={
                            "data": graphs.graph_4(countrylist)[0],
                            "layout": graphs.graph_2(countrylist)[1]
                        })
    elif graphlist == 'Population Value Table':
        return dcc.Graph(id='display-map', 
                            figure={
                            "data": graphs.graph_5()[0]
                        })
    elif graphlist == 'Annual Population Growth':
        return dcc.Graph(id='display-map', 
                            figure={
                            "data": graphs.graph_6()[0],
                            "layout": graphs.graph_6()[1]
                        })
    elif graphlist == 'Population Growth Rate':
        return dcc.Graph(id='display-map', 
                            figure={
                            "data": graphs.graph_7()[0],
                            "layout": graphs.graph_7()[1]
                        })
    

#----------------------------Tab 3----------------------------#
def tab3GraphsFunctionCall(graphlist, countrylist):
    if graphlist == 'GDP per Capita Trend':
        return dcc.Graph(id='display-map', 
                            figure={
                            "data": graphs.graph_8(countrylist)[0],
                            "layout": graphs.graph_8(countrylist)[1]
                        })
    elif graphlist == 'GDP per Capita Value':
        return dcc.Graph(id='display-map', 
                            figure={
                            "data": graphs.graph_9()[0],
                            "layout": graphs.graph_9()[1]
                        })
   
    
#----------------------------Tab 4----------------------------#
def tab4GraphsFunctionCall(graphlist, countrylist):
    if graphlist == 'Country-wise Trend for EF vs BC':
        return dcc.Graph(id='display-map', 
                            figure=graphs.graph_10(countrylist))
    elif graphlist == 'Entire UN Region EF vs BC Analysis':
        return dcc.Graph(id='display-map', 
                            figure=graphs.graph_11(countrylist))
    elif graphlist == 'Country-wise Deficit vs Reserve':
        return dcc.Graph(id='display-map', 
                            figure=graphs.graph_12(countrylist))
    elif graphlist == 'Ecological Deficit and GDP':
        return dcc.Graph(id='display-map', 
                            figure={
                            "data": graphs.graph_13(countrylist)[0],
                            "layout": graphs.graph_13(countrylist)[1]})
    
#----------------------------Tab 5----------------------------#
def tab5GraphsFunctionCall(graphlist, countrylist):
    if graphlist == 'Earth Overshoot Day':
        return dcc.Graph(id='display-map', 
                            figure={
                            "data": graphs.graph_14()[0],
                            "layout": graphs.graph_14()[1]})
    elif graphlist == 'Carbon Footprint Analysis':
        return dcc.Graph(id='display-map', 
                            figure={
                            "data": graphs.graph_15(countrylist)[0],
                            "layout": graphs.graph_15(countrylist)[1]})