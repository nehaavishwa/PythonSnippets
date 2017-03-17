import urllib
import pandas as p
import csv

url = "http://www.calvin.edu/~stob/data/Berkeley.csv"
df = p.read_csv(url)
print(df[:10])
df1 = df.groupby('Admit').sum()
#print(df1)
df3 = df.groupby('Gender').sum()
print(df3)
df2 = df.groupby(['Admit', 'Gender']).sum()
print(df2/df3*100)


df4 = df.groupby(['Admit', 'Gender', 'Dept']).sum()
print(df4/df3*100)