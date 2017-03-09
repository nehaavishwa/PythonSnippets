__author__ = 'nvishwakarma'
import random as r

'''this is some file 1'''
'''
Write a function that takes a list of positive integers as an input, and returns all of the pairs of integers it contains
that sum to 100. You can assume that all inputs are between 1 and 99.

Example Inputs and Outputs:

[ 1, 98, 99 ] => [ [1, 99] ]
[ 95, 5, 95 ] => [ [ 5, 95 ] ]
[ 95, 5, 95, 5 ] => [ [ 5, 95 ], [ 5, 95 ] ]
[ 95, 5, 95, 5, 10, 90 ] => [ [ 5, 95 ], [ 5, 95 ], [10, 90] ]
[5, 5, 10, 90, 95, 95]

import random as r

def SumFind():
    l=[]
    for i in range(1,100):
        l.append(r.randrange(3,100))
        l.sort()

    for i in range(1, len(l)-1):
        x = 100-l[i]
        if x in l:
            print(x, l[i])
            continue
    print(l)


SumFind()'''


def SumFind():
    l = [95, 5, 95, 5, 10, 90]
    l1 = []
    '''for i in range(1,100):
        l.append(r.randrange(3,100))'''
    l.sort()

    for i in range(1, len(l)-1):
        x = 100-l[i]
        for i1 in range(0, len(l1)):
            if x in l:
                print(x, l[i])
                l1.append(x)
                l1.append(l[i])

    print(l)


SumFind()
