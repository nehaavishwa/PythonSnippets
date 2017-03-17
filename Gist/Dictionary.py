'''Problem
You want to make a dictionary that maps keys to more than one value (a so-called
“multidict”).
'''

from collections import defaultdict


def multiDict(pairs):
    d = defaultdict(list)
    for key, value in pairs:
        print(key, value)
        d[key].append(value)
    return d

d = {
'a' : [1, 2, 3],
'b' : [4, 5]
}
e = {
'a' : {1, 2, 3},
'b' : {4, 5}
}
#a = multiDict(['1', '2'])
#print(a)

'''Keeping Dictionaries in Order'''

from collections import OrderedDict

#d = OrderedDict()
d ={}
d['1'] = 'foo'
d['2'] = 'bar'
d['6'] = 'da'
d['4'] = 'baa'
d['5'] = 'oink'
d['3'] = 'yee'

for key in d:
    print(key, d[key])




'''Calculating with Dictionaries'''
prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

min_prices = min(prices.values())
print(min_prices, min(zip(prices.values(), prices.keys())))
price_sorted = sorted(zip(prices.values(), prices.keys()))
print(price_sorted)


'''Finding Commonalities in Two Dictionaries'''

a = {
'x' : 1,
'y' : 2,
'z' : 3
}
b = {
'w' : 10,
'x' : 11,
'y' : 2
}

x = a.keys()& b.keys()
print(x)
x = a.keys()- b.keys()
print(x)
x = a.items()- b.items()
print(x)

c = {key: a[key] for key in a.keys()-{'z'}}
print('===')
print(c)

import math
x = 1
x1 = (lambda x: x*2)(1)
print(x1)

square_root = lambda x: math.sqrt(x)
print(square_root(100))

record = '....................100 .......513.25 ..........'
cost = int(record[20:32])
print('cost=',cost)
'''
d = {'1': 'a', '2': 'b'}
for ke, val in d.items():
    print(ke, val)
print(d)
'''