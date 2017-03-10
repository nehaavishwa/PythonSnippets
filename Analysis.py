import pandas as p
import numpy as np

filename = r'C:\PersonalProjects\PythonSnippets\YoungPeople\Files\responses.csv'


df = p.read_csv(filename, dtype='unicode', usecols=['Finances', 'Shopping centres', 'Branded clothing', 'Entertainment spending',
       'Spending on looks', 'Spending on gadgets',
       'Spending on healthy eating', 'Age', 'Height', 'Weight',
       'Number of siblings', 'Gender', 'Left - right handed', 'Education',
       'Only child', 'Village - town', 'House - block of flats'])

df.dropna(how='all')
df.rename(columns={'Shopping centres': 'Shopping_Centres', 'Branded clothing': 'Branded_Clothing'
                                      , 'Entertainment spending': 'Entertainment_Spending', 'Spending on looks': 'Spending_On_looks'
                                      , 'Spending on gadgets': 'Spending_on_gadgets'
                                      , 'Spending on healthy eating': 'Spending_on_healthy_eating', 'Only child':'Only_child', 'Number of siblings': 'Number_of_siblings'}, inplace=True)
df_MV = df.fillna({1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 'NA', 9: 'NA', 10: 'NA', 12: 'NA', 13: 'NA', 14: 'NA', 15: 'NA', 16: 'NA', 17: 'NA'})


'''
print(df[['Spending_on_healthy_eating', 'Age', 'Height', 'Weight',
       'Number of siblings', 'Gender', 'Left - right handed', 'Education',
       'Only child', 'Village - town', 'House - block of flats']][:20])
'''
'''
print(p.DataFrame(df[:10], columns=['Age', 'Number of siblings','Only child', 'Gender',
        'Village - town', 'House - block of flats', 'Spending_On_looks']))
'''

'''
#Demographics - who says they are the only child yet # of siblings is greater than 0: Are they lying
df1 = df_MV[(df_MV['Only_child'] == 'yes') & (df['Number_of_siblings'] > '0')][['Gender', 'Age', 'Only_child', 'Number_of_siblings', 'Education']][:15]
print(df1)
'''

#Spending across Gender
#df_MV = df_MV[['Gender', 'Finances', 'Spending_on_gadgets','Shopping_Centres', 'Branded_Clothing', 'Entertainment_Spending', 'Spending_On_looks', 'Spending_on_healthy_eating']].apply(lambda x: p.to_numeric(x, errors='ignore'))
#df_MV_grouped = df_MV.groupby(['Gender']).mean()

#Spending across Gender and Age
df_MV = df_MV[['Gender','Age', 'Finances', 'Spending_on_gadgets','Shopping_Centres', 'Branded_Clothing', 'Entertainment_Spending', 'Spending_On_looks', 'Spending_on_healthy_eating']].apply(lambda x: p.to_numeric(x, errors='ignore'))
df_MV_grouped = df_MV.groupby(['Gender', 'Age']).mean()
print(df_MV_grouped[:5])
#print('\n\n', df_MV.groupby(['Gender', 'Age']).size())
#print(df1[['Gender', 'Age', 'Only_child', 'Number_of_siblings', 'Education']])
