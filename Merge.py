import pandas as pd

#laodfiles
file1 = pd.read_csv('filename')
file2 = pd.read_csv('filename')

#viewfiles
file1.head()
file2.head()

#Merge files together with an inner join 
combo = pd.merge(file1, file2, on='ID', how='inner')


#view new data
combo.head()


#Send to csv
combo.to_csv('C:\Users\Jgarson\Documents\combo.csv', index=False)




