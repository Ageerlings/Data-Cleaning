#lets load this into a dataframe.
import pandas as pd
import numpy as np
df = pd.read_csv('combined_2.csv', encoding = "ISO-8859-1",parse_dates=['Date'], dayfirst=True, index_col='Date',dtype={"Column Name": float})
df[:3] #take a look at the data DataFrame


df.dtypes # take a look at the columns and their respective data types
