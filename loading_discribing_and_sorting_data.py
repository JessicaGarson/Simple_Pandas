import pandas as pd

#laodfiles
df = pd.read_csv('filename')

#view the data
df.head()

#get stats on your data
df.describe()

#sorting your dataframe by a column 
df.sort(columns='column_name')
