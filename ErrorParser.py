__author__ = 'nvishwakarma'
import re
#import csv
import pandas as p

filePath = r'C:\PersonalProjects\PythonSnippets\Files\SurveyInvalid.txt'
s_proc=set()




def parser(file):
    with open(file, 'r') as f:
        for line in f:
            search = re.search(r'Procedure.*[,]',line)
            search1 = re.search(r'module ''.*depends \'',line)
            #print(search.group())
            if search:
                s_proc.add(search.group())

            if search1:
                s_proc.add(search1.group())
                #print(search.group())
    return sorted(s_proc)


file =r'C:\Users\nVishwakarma\Documents\SQL Server Management Studio\Projects\UnusedObject\TransUnused.xlsx'
fileOpen = open(file, 'wb')
lst=[]
x1 = parser(filePath)
for i in x1:
    if(i !='Procedure fEvalQuestionLabel,'):
        #UnusedObj.writerow([i.replace('Procedure', '').replace('module', '').replace('depends','').strip()])
        lst.append(i.replace('Procedure', '').replace('module', '').replace('depends','').strip())
        frame = p.DataFrame(lst)
        frame.to_excel(file)
