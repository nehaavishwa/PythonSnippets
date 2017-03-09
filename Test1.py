import pandas as p
import numpy as np
import re
import matplotlib.pyplot as m

from pandas.io.parsers import read_csv


Diagnostics = r'C:\PersonalProjects\PythonSnippets\Indeed\Files\DiagnosisCodes.csv'
df_Diagnostics = read_csv(Diagnostics)

NEISS2014 = r'C:\PersonalProjects\PythonSnippets\Indeed\Files\NEISS2014.csv'
df_NEISS2014 = read_csv(NEISS2014)

df = df_NEISS2014.set_index('diag').join(df_Diagnostics.set_index('Code'), on=None, how='outer', sort=True)
df.rename(columns={'CPSC Case #': 'a', 'trmt_date': 'b'}, inplace=True)
print(df[:5])
df1 = df.groupby(['Diagnosis', 'disposition']).size().to_frame('Count')

#print(df1)
#print(df[df['Diagnosis'] == 'Ingested foreign object'])