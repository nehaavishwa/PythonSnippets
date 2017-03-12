__author__ = 'nvishwakarma'
import pandas as p
import numpy as np
from pandas import read_csv


filepath = r'C:\PersonalProjects\PythonSnippets\YoungPeople\Files\responses.csv'
df_fulldataset = p.read_csv(filepath,  dtype='unicode'#, nrows=5
                          , usecols=[140, 141, 142, 143, 144, 145, 146,
                                     147, 148, 149, 139, 138, 137, 136, 135, 134, 133])
print(df_fulldataset.columns, '\n')
#print('\n', df_fulldataset.columns, '\n', df_fulldataset[:10])
df_fulldataset[['Finances', 'Shopping centres', 'Branded clothing',
       'Entertainment spending', 'Spending on looks', 'Spending on gadgets',
       'Spending on healthy eating']] = df_fulldataset[['Finances', 'Shopping centres', 'Branded clothing',
       'Entertainment spending', 'Spending on looks', 'Spending on gadgets',
       'Spending on healthy eating']].astype(float)
#print(df_fulldataset[:2])
#print(df_fulldataset.shape)
#df_test = df_fulldataset[['Finances', 'Gender', 'Shopping centres']]
#print('\n', df_test.dropna(how='all'))
#df_test = df_test.dropna(how='all')
#print(df_test.fillna({1: 0, 2: 'NA'}))
#df_test = df_test.fillna({'Finances': 0,'Shopping centres': 0, 'Gender': 'NA'})
#df_test.rename(columns={'Shopping centres': 'Shopping_Centres', 'trmt_date': 'Date'}, inplace=True)
#print(df_fulldataset[:5])
#df_test = df_test[df_test['Gender'] == 'NA'] or df_test[df_test['Shopping_Centres']==1]
#print(df_test[df_test['Shopping_Centres']==1][:5])
#print(#df_fulldataset.isnull(),
  #   p.isnull(df_test))
#print(#df_fulldataset.isnull(),
 #     p.isnull(df_fulldataset))

df_fulldataset = df_fulldataset.dropna(how='all')
df_fulldataset.rename(columns={'Shopping centres': 'Shopping_Centres', 'Branded clothing':'Branded_Clothing'
                                       ,'Entertainment spending':'Entertainment_Spending', 'Spending on looks' : 'Spending_On_looks'
                                        , 'Spending on gadgets':'Spending_on_gadgets'
                                        ,'Spending on healthy eating':'Spending_on_healthy_eating'}, inplace=True)
df_fulldataset.fillna({1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 'NA', 9: 'NA', 10: 'NA', 12: 'NA', 13: 'NA', 14: 'NA', 15: 'NA', 16: 'NA', 17: 'NA'})
print(df_fulldataset[:2])
'''
grouped_Gender = df_fulldataset.groupby(['Gender']).sum()
print(grouped_Gender)
'''
#print(grouped_Gender.sort_values(['Count'], ascending=False))
