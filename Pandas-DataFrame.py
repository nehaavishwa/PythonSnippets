__author__ = 'nvishwakarma'
import pandas as pd

obj = pd.Series([3, 4, 6, -2])
#print(obj, obj.values, obj.index)

obj2 = pd.Series([3, 4, 6, -2], index=['a', 21, 3, 4])
obj['a'] = 8
print(obj2[:3])

dict_data = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000}
ss = pd.Series(dict_data)
print(ss)

x = [1, 2, 3]
sd = pd.Series([2, 3, 4], index=x)
print(sd)
