__author__ = 'nvishwakarma'


list =[]
str =''
path = r'C:\PersonalProjects\PythonSnippets\Files\List'
fo = open(path, 'r')
for i, line in enumerate(fo,1):
    #print(i, line)
    if i>1:

        x = line.split(' ')
        str = x[0]
        print(x[0], x[1])
        if str == 'insert':
            list.insert(0, 5)
            print(list)


fo.close()