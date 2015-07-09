import pandas as pd

#importing a csv with a header row
csv = pd.read_csv('file_name.csv', header=0)

#loading in from excel 
excel = pd.read_excel('file_name.xlsx', sheetname='Sheet2')

#getting simple information on our dataframes 
csv.info()
excel.info()
