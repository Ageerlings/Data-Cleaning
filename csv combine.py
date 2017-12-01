# combines my multiple csv files into one
# removes the headers in the files after the first file,
import glob as glob
path =r'C:\Users\ageerlings\data' # use your path
allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0, encoding='latin-1') # you may need to adjust your encoding to something else
    list_.append(df)
frame = pd.concat(list_)
frame.to_csv('data_12.csv', sep=',', encoding='utf-8', index=False) #saves a csv
frame.shape # checks the size of the file
