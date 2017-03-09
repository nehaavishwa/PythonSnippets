__author__ = 'nvishwakarma'

def  StairCase(n):
    for i in range(n, ):
        print(''*i, 'x')
        for x in range(0, i):
            print('x')


#StairCase(6)


def summation(numbers):
    sum =0
    for i in range(0, len(numbers)):
        if i !=0:
            sum = sum+numbers[i]
    print(sum)

a = 2,12,12
#summation(a)

#print(sum([0, 5, -1]))
-5 -1 -3

l = []
def  getSequenceSum(i, j, k):
    if j <0 and i < 0:
        for x in range(i, j+1):
            l.append(x)
        if(k<0):
            for x1 in range(j-1, k-1, -1):
                l.append(x1)
        else:
            for x1 in range(j, k):
                l.append(x1)
        sum1 = sum(l)
        print(l)
        print(sum1)

getSequenceSum(-5, -1, -3)
getSequenceSum(0, -5, -1)