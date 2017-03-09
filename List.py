__author__ = 'nvishwakarma'
import time;
#from ReturnStatement import addition
import ReturnStatement

#print(ReturnStatement.addition(10, 20, 30))
#print(ReturnStatement.substraction(10, 20))

'''
def is_leap(year):
    leap = False

    # Write your logic here
    if year % 100 == 0 and year % 400 == 0:
        leap = True
    elif year % 4 == 0:
        leap = True
    else:
        leap = False
    return leap
'''


list =[]
path = r'C:\PersonalProjects\PythonSnippets\Files\List'
fo = open(path, 'r')
for i in fo:
    print(i)
fo.close()


'''
days = ['Sunday', 'Monday', 'Wednesday']
print(days[1])
numbers = [1, 2, 3, 4, 5, 6, 12, 14]
print(numbers[1:5])
days[2] = 'January'
print(days)
del days[2]
print(days)

#Slicing works as string
print(days[-2])
print(days[-1])

months = ['Sunday', 'Monday', 'Wednesday']
print(len(days))
print(max(days))
print(min(days))
#print(cmp(days,months))
ticks = time.time()
print(ticks)
currenttime = time.localtime(time.time())
print("Current local time:", currenttime)


def listFunction1(elelist):
    elelist.append([1,2,3])
    print("Append",elelist)
    return


def listFunction2(elelist):
    elelist[2] = 50
    print("Overwritten", elelist)
    return


elelist = [100, 200, 300]
listFunction1(elelist)
print("Function1", elelist)

listFunction2(elelist)
print("Function2", elelist)


def printInformation(arg1, *varagrs):
    print(arg1)
    for i in varagrs:
        print(i)
    return ;


printInformation(3423)
printInformation('rgreg', 10, 90)
'''
#Lambda Expressions

