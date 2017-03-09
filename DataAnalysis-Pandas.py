__author__ = 'nvishwakarma'

from pandas import DataFrame
import pandas as pd
import json
import matplotlib as plt


plt.interactive(False)

path = r'C:\PersonalProjects\PythonSnippets\Files\usagov.txt'
records = [json.loads(line) for line in open(path)]
frame = DataFrame(records)
##print(frame['tz'][:10])


clean_tz = frame['tz'].fillna('Unknown')
clean_tz[clean_tz == ''] = 'Unknown'
#print(clean_tz[:100])

tz_counts = clean_tz.value_counts()
print(tz_counts[:10])

#plt.tz_counts[:10].plot(kind='barh', rot=0)
print(frame['a'][1])
print(frame['a'][50])
