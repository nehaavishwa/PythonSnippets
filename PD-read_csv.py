__author__ = 'nvishwakarma'

from pandas.io.parsers import read_csv
import numpy as np

df = read_csv(r"C:\PersonalProjects\PythonSnippets\Files\WHO_first9cols.csv")
#print("DataFrame", df)
'''print("Shape", df.shape)
print("Length", len(df))

print("Column Headers", df.columns)
print("Data Types", df.dtypes)
print("Index", df.index)
print("Values", df.values)'''

country_col = df["Country"]
'''print("Type of DF", type(df))
print("Type of Country_Col", type(country_col))
print("Series Shape", country_col.shape)
print("Series Index", country_col.index)
print("Series value", country_col.values)
print("Series Name", country_col.name)'''

#print("Last 2 countries:", country_col[-5:])
#print("df signs", np.sign(df))
last_col = df.columns[-1]
#print("Last df column signs", last_col, np.sign(df[last_col]))
print(df[last_col])#,
print(df[last_col].values)
#print(np.sum(df[last_col] - df[last_col].values))
#print(np.sum(df[last_col] - df[last_col].values))







