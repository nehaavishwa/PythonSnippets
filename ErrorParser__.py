__author__ = 'nvishwakarma'
import re
import csv


file = r'C:\PersonalProjects\PythonSnippets\Files\SurveyInvalid.txt'
s_proc=set()



with open(file, 'r') as f:
    for line in f:
        search = re.search(r'Procedure.*[,]', line)
        search1 = re.search(r'module ''.*depends \'', line)
        if search:
                s_proc.add(search.group())
                print(search.group())

        if search1:
                s_proc.add(search1.group())
                print(search1.group())
    
            
          


