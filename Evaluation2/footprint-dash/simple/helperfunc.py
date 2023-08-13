import math

def extract_country_by_record(df, country_name, record):
    country_foot_print=df[df.country.isin([country_name])]
    country_by_record = country_foot_print [country_foot_print.record.isin([record])]
    return country_by_record

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
    return feature_values, available_countries, excluded_countries 

# def print_excluded_countries (excluded_countries,year):
#     if len(excluded_countries) != 0:
#         # print("excluded countries from dataset in {0} are : ".format(year))
#         for i in excluded_countries:
#             # print(i)   
            
def calculate_growth_rate(present,past,period):
    #present : present year , past: past year , period: number of years between present and past
    percentage_growth_rate = ((present - past)/(past*period))*100
    return percentage_growth_rate