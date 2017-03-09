__author__ = 'nvishwakarma'
import random as r

def casing():
    s ='Www.HackerRank.com' #'HackerRank.com presents "Pythonist 2".'
    x = ''
    for i in range(0, len(s)):
        if s[i].islower():
            a = s[i].upper()
        else:
            a = s[i].lower()
        x = x + a
        #print(x)
    print(x)


def splitJoin():
    x1=''
    s = 'this is a string'
    x = s.split()
    x1 = '-'.join(x)
    print(x1)

def stringM():
    string = input("Enter String here:")
    i = int(input("Enter a # here"))
    c = str(input("Enter a character here"))
    lst = list(string)
    lst[i] = c
    string = ''.join(lst)

    print(string)


def stringSepM():
    string = "Enter String here:"
    i = '1 F'
    c1 = i.split()
    c=c1[1]
    lst = list(string)
    lst[int(c1[0])]=c
    string = ''.join(lst)
    print(string)


def finder(l, a):
    if a in l:
        return 1


def strCom():
    s = 'ABCDCDC'
    sub = 'CDC'
    x = 0

    print(s)
    for i in range(0, len(s)):
        if s[i:i+3] == sub:
            x = x+1
    print(x)


def MicAvg():
    #i = int(input())
    s=set()
    l=[161, 182, 161, 154, 176, 170, 167, 171, 170, 174]
    for i in l:
        s.add(i)
    '''for i1 in range(0,i):
        x = int(input())
        s.add(x)'''
    print(s)
    print(len(s))
    avg = sum(s)/len(s)
    print(avg)


def AddToSet(a, b, n):
    for i in range(0, n):
        a.add(r.randrange(i, n))
    #print(a, len(a))

    while (len(b)!=len(a)):
        x = r.randrange(0, n*100)
        if x not in a:
            b.add(x)
    #print(b)
    return a, b


def setAB():
    #t=(1,2,3,4,5)
    a = set()
    b = set()
    H = 0
    arr = [1, 2, 3, 56, 21]
    a, b = AddToSet(a, b, 3)
    print(a, b)
    for i in arr:
        if i in a:
            H = H+1
        if i in b:
            H= H-1
    print(H)


def SetAdd():
    i = int(input())
    s = set()
    for i1 in range(0, i):
        while(len(s)!=i):
            c = str(input())
            if c.isalpha():
                s.add(c)
            else:
                print('Enter Again')
                continue;
    print(len(s))








#SetAdd()
#setAB()
#MicAvg()
#casing()
#splitJoin()



