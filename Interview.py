__author__ = 'nvishwakarma'

'''
a = 10
b = list(a)
print(b)
#b = int(b) + 10
print(b)
'''


xList = [1, 2, 6, 4, 8]
b = []
x = 0


def oddPos(a):
    for i, x in enumerate(a):
        #print(i, x)
        if i % 2 != 0:
            #print(i, a[i])
            b.append(a[i])
    return b


#a = oddPos(xList)
#print(a)

#assert oddPos([0, 1, 2, 3, 4, 5]) == [1, 3, 5]


def sumElement(a):
    x = 0
    for i in a:
        #print(i)
        x += i
    return x


s = sumElement(xList)
print(s)

'''
x = 2
y = 3
z = x**y
print(z)

#Binary Operator
#
x = 8
y = 13
print(~y)
print(~x)

print(x<<1)
print(x>>1)
'''
'''
a = 'AB'
c = int(a[1])
print(c)
'''


