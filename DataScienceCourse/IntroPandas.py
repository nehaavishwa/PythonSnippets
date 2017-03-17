import pandas as p

Series = p.Series(['Alex', 'Hsing', 'Rob', 'Jason'])
print(Series)

Series = p.Series(['Alex', 'Hsing', 'Rob', 'Jason'], index=['Instructor', 'Curriculum Manager',
                              'Course Number', 'Power Level'])
print(Series[['Instructor', 'Curriculum Manager']])

cuteness = p.Series([1, 2, 3, 4, 5], index=['cake', 'boss', 'damn', 'loyo', 'peela'])
print(cuteness[cuteness > 3])

comments = 'This is a test where I want to count the word test lets how test is counted'
l1 = comments.split(' ')
print(l1)
l2 = []
for i in l1:
    if i == 'test':
        l2.append(i)

print(l2, len(l2))

data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = p.DataFrame(data)
print("DataType=",football.dtypes)
print("")
print(football.describe())
print("")
print(football.head())
print("")
print(football.tail())
