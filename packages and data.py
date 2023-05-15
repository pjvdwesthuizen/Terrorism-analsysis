#Terrorism regression analysis. 

#Packages being used in this script.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns


#Intention for this script: 
#I am going to perform regression analysis to determine which factors can lead to a rise in fatalities from terrorism. 
#The terrorism related fatalities data is from ourworldindata.com. 
#GDP data is from the World bank. 


#Importing dataset. 
#Number of fatalities caused by terrorism - data set from ourworldindata (https://ourworldindata.org/terrorism#terrorism-deaths-globally)

terrorism_data  = pd.read_csv(r'C:\\Users\\pjvdw\\Desktop\\terrorism\\fatalities-from-terrorism.csv')

#GDP per capita in current US$ from world bank data (https://data.worldbank.org/indicator/NY.GDP.PCAP.CD)

GDPPC = pd.read_csv(r'C:\\Users\\pjvdw\\Desktop\\terrorism\\gdp data\\API_NY.GDP.PCAP.CD_DS2_en_csv_v2_5454904.csv', on_bad_lines= 'skip')

#Things to do for data: 
#terorrism data - clean - only use countries with data for both 2000 and 2020 - exclude all else. 
#gdp data - (1) eliminate countries not in terrorism data (2) eliminate data from before 2000 and after 2020. 

#Terorism data: 

#Data only goes up to 2020. 
#Want to eliminate countries that don't have data points that go up to 2020. 
#Need to eliminate all data points prior to 2000 for a conisistent measurement. 

#Printing the columns so that I know what data I can call on. 
print(terrorism_data.columns)

#Cleaning up terrorism fatalities data - removing duplicate data and excluding pre-2000 data. 

terrorism_data.drop_duplicates()


terrorism_data
#merging the data gdp and terrorism data sets. 

print(GDPPC.columns)
