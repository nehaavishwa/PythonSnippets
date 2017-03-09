__author__ = 'nvishwakarma'
import numpy as n
#Given [3, 30, 34, 5, 9], the largest formed number is 9534330

a = n.array([0, 1, 2,3], dtype=n.int)
a.sort()

def largestNumber(a):
    b = []
    #print(a, a[0], a[1])
    for i in a:
        str1 = ''
        str1 = str(i)
        for l in str1:
            x = int(l)
            b.append(x)
    b1 = n.array(b)
    b1.sort()
    #print(b1)
    return b1


a = largestNumber([1, 55, 4])
print(a)
