# Holding random things here
,dtype={"Standard Cost": float}
df.applymap(np.isreal)
#df.replace('\'', '') #lets rip out the quotes

#reads my csv and makes sure it can load
import csv
with open('combined_2.csv', 'r') as f:
    reader = csv.reader(f)

    for row in reader:
            print (row)

# gives a T/F result for each row based on the data entered
df['Column Name'].str.contains('What you want to search for')

#checks the DF to see if the data is real
np.argmin(df.applymap(np.isreal).all(1))



#lets clean up our dataframe
df[['Standard Cost']].apply(pd.to_numeric, errors='raise') #working?
df['Standard Cost'].replace('', np.nan, inplace=True)
df.dropna(axis=1, how='any') #drops null rows
df.dropna(subset=['Standard Cost'], inplace=True)
pd.DataFrame(df, columns=['Standard Cost'], dtype=float) #not working
df[:16]



# combines my multiple csv files into one
#does not remove the headers
#just uses python and not any imported packages
fout=open("combined_2.csv","a")
# first file:
for line in open("data1.csv"):
    fout.write(line)
# now the rest:
for num in range(2,14):
    f = open("data"+str(num)+".csv")
    next(f) # skip the header (this does not work it seems)
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()
