__author__ = 'nehaavishwa'
# Enter your code here. Read input from STDIN. Print output to STDOUT

def inp_1():
    Num = int(input())
    Name_Marks = []
    for i in range(0, Num):
        Name = str(input())
        Marks = int(input())
        x = "x"+str(i)
        x = []
        x.append(Name)
        x.append(Marks)
        Name_Marks.append(x)
    return Name_Marks
    #Name_Marks.append(Marks)

def get_high(Name_Marks):
    #for i in range(0,len(Name_Marks)):
    for k in Name_Marks:
        print(k)


Name_Marks = inp_1()
get_high(Name_Marks)
#print(Name_Marks[0][0])

'''
5
Helen
34
Raji
56
Bolu
90
Natalie
45
Jin
32
'''
