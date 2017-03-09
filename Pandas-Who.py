__author__ = 'nvishwakarma'

from pandas.io.parsers import read_csv
import numpy as np

file = r'C:\PersonalProjects\PythonSnippets\Files\WHO.csv'
df = read_csv(file)
#print("Dataframe:", df[0:2])

'''print("Shape", df.shape)
print("Length", len(df))
'''

#print("Column Headers", df.columns)
#print("Data types", df.dtypes)
#print("Index", df.index)
#print("Values", df.values)

'''
country_col = df['Country']
print(country_col[0:2])
print(type(country_col))
print("Series shape", country_col.shape)
print(country_col.name)
'''

#print("df signs", np.sign(df['Urban_population_growth'][1:5]))
last_col = df.columns[-1]
last_col1 = df.index[-1]
#print(np.sign(df[last_col][1:1]))
print(df.loc[last_col1])





