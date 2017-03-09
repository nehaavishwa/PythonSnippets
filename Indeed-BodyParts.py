__author__ = 'nvishwakarma'
import pandas as p
import numpy as np
from pandas.io.parsers import read_csv

BodyParts = r'C:\PersonalProjects\PythonSnippets\Indeed\Files\BodyParts.csv'
df_BodyParts = read_csv(BodyParts)
df_BodyParts = df_BodyParts[:-3]
NEISS2014 = r'C:\PersonalProjects\PythonSnippets\Indeed\Files\NEISS2014.csv'
df_NEISS2014 = read_csv(NEISS2014)
df = df_NEISS2014.set_index('body_part').join(df_BodyParts.set_index('Code'), on=None, how='left', sort=True)
#print(df.shape)
#print(df[['BodyPart','sex', 'race']][1:10])
grouped = df.groupby('BodyPart')#.agg({'count': sum})
grouped1 = grouped.size()
df_grouped = grouped1.to_frame('BodyParts')
print(df_grouped.sort_values(['BodyParts'], ascending=False)[:3])
print(df_grouped.sort_values(['BodyParts'], ascending=True)[:3])