__author__ = 'nehaavishwa'

'''M = input()
M1 = list(input())
M2 = list(input())'''

'''5
9
11
12'''


def insSort(li):
    for i in range(0,len(li)):
            j = i
            while j>0 and int(li[j-1]) >int(li[j]):
                li[j], li[j-1] = int(li[j-1]), int(li[j])
                j = j-1

    return li


M1 = '2 4 5 9'
M2 = '2 4 11 12'
M1 = M1.split(' ')
M1 = set(M1)
M2 = M2.split(' ')
M2 = set(M2)
print(M1, M2)

N = set()
M11 = M1.difference(M2)
M21 = M2.difference(M1)

N = M11.union(M21)
N = list(N)
N = insSort(N)


#N = map(int, N)


print(N)




