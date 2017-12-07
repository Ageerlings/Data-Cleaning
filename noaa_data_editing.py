# script for editing NOAA weather data downloads and getting rid of unneeded columns.
import pandas as pd
import numpy as np
import datetime as dt

df = pd.read_csv('1144127.csv') #load csv into a dataframe
df_2 = df.filter(['STATION','STATION_NAME','ELEVATION','LATITUDE','LONGITUDE','DATE','HOURLYDRYBULBTEMPF','HOURLYPrecip'], axis=1) #filter df to a new df with selected collumns 
df_2['DATE'] = pd.to_datetime(df['DATE']) #converts date column from object into date
df_2['DATE'] = df_2['DATE'].apply(lambda dt: datetime.datetime(dt.year, dt.month, dt.day, dt.hour)) #converts date column timestamsp and rounds to the hour.
df_2['HOURLYPrecip'].fillna(0, inplace=True) # replaces nulls in the percepitation with zeros
df_2.to_csv('weather_data_1.csv', header = True, sep=',') # dumps dataframe into a new csv
