__author__ = 'nvishwakarma'

import pandas as p
from pandas.io.parsers import read_csv

path = r'C:\PersonalProjects\PythonSnippets\Indeed\Files\BodyParts.csv'
df = read_csv(path)
y1 = p.DataFrame(df.BodyPart.str.replace(r',\s[A-Za-z]+', ''))
#print(type(y1), type(df))
y2 = y1.groupby(['BodyPart'], sort=False).size()
y3 = y1.groupby('BodyPart').count()
#y4 = y3[['BodyPart']].transform(max).sort('BodyPart')

#y2.sort([]
print(y2)
'''
print(df['BodyPart'].groupby(df['BodyPart']))
grouped = df['BodyPart'].groupby(df['BodyPart'])
print(grouped.mean)
'''
'''
k = df.replace(['lower'],[' '])
#k = df['BodyPart'].str[0:str.find(',', 0)]
#print(k)

s = df['BodyPart'].str.split(', ').apply(p.Series, 1).stack()
s.index = s.index.droplevel(-1)
s.name = 'BodyPart'
#print(s)

y = df.join(s.apply(lambda x: p.Series(x.split(','))))
#print(y)
x = p.concat([p.Series(row['Code'], row['BodyPart'].split(','))
                    for _, row in df.iterrows()]).reset_index()
#print(x)

'''
str = 'Arm, Lower'
#df1 = p.DataFrame(str)
y = str.replace(str[str.find(','):len(str)],'')


