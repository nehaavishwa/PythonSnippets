__author__ = 'nehaavishwa'

import numpy as n

""" Use below to install numpy"""
# sudo pip3 install numpy

'''

How is numpy more efficient?
So, in Mathematics if we add scalar values we are performing scalar addition,
In any programming language we will have to put them in an array and then iterate through it which becomes more verbose
than how we do things in mathematics.

In mathematics, we treat the addition of two vectors as a single operation. That's the way NumPy arrays do it too,
and there are certain optimizations using low-level C routines, which make these basic operations more efficient.

'''
'''
In function below, this is how this is done any programming language
'''
def pSum(n):

    a = list(range(n))
    b = list(range(n))
    c = []

    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3

        c.append(a[i]+b[i])

    return c


'''Below is how this is done in numpy and no loop is required'''
def numpySum(m):
    d = n.arange(m) ** 2
    e = n.arange(m) ** 3
    f = d + e
    return c

c = pSum(1000)
print(c)

f = numpySum(1000)
print(f)
