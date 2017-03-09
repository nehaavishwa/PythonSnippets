def checkInp(li, x):
    if len(li) != x:
        return 0
    else:
        return 1


def insSort(x, li):

    ret = 1 #checkInp(li, x)
    if ret ==1:
        #li = map(int, li)
        for i in range(0,len(li)):
            j = i
            '''if j>0 and int(li[j-1]) == int(li[j]):
                li.remove(li[j-1])'''
            while j>0 and int(li[j-1]) >int(li[j]):
                li[j], li[j-1] = int(li[j-1]), int(li[j])
                j = j-1
    else:
        print("Try Again")
    return li

    

x = int(input())
a = set()
li = str(input())
li = li.split(' ')

for i in range(0,len(li)):
    a.add(li[i])

a = list(a)
#li = a
li = insSort(x, a)
print(type(a))
print(li)
print(li[len(li)-2])




