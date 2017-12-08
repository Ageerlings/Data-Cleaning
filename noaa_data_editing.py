# script for editing NOAA weather data downloads and getting rid of unneeded columns.
#You can also just continue to edit this in the dataframe and do analysis instead of dumping into a csv should you not need a csv.
import pandas as pd
import numpy as np
import datetime as dt

df = pd.read_csv('1144127.csv') #load csv into a dataframe
df_2 = df.filter(['STATION','STATION_NAME','ELEVATION','LATITUDE','LONGITUDE','DATE','HOURLYDRYBULBTEMPF','HOURLYPrecip'], axis=1) #filter df to a new df with selected collumns
df_2['DATE'] = pd.to_datetime(df['DATE']) #converts date column from object into date
df_2['DATE'] = df_2['DATE'].apply(lambda dt: datetime.datetime(dt.year, dt.month, dt.day, dt.hour)) #converts date column timestamsp and rounds to the hour.
df_2['HOURLYPrecip'].fillna(0, inplace=True) # replaces nulls in the percepitation with zeros
df_2['HOURLYDRYBULBTEMPF'] = df_2['HOURLYDRYBULBTEMPF'].str.extract('(\d+)', expand=False) # removes the random non numeric characters from the column
df_2['HOURLYDRYBULBTEMPF'] = pd.to_numeric(df_2['HOURLYDRYBULBTEMPF']) #converts the object column to numeric
df_2.to_csv('weather_data_1.csv', header = True, sep=',') # dumps dataframe into a new csv




# Plot a graph
df_2.plot(x='DATE', y='HOURLYDRYBULBTEMPF', style='o')

# not working, trying to use df_2 and fiter then graph
df_2.loc[(df_2.STATION == 'WBAN:53884'), ['DATE','HOURLYDRYBULBTEMPF']].plot






# make a new df for one station and graph
df_3 = df_2.loc[lambda df_2: df.STATION == 'WBAN:03822']
df_3.plot(x='DATE', y='HOURLYDRYBULBTEMPF', style='o')
