__author__ = 'nvishwakarma'
import pymongo
import csv
from pymongo import MongoClient

conn = pymongo.MongoClient('mongodb://nvishwakarma:MMNvishwakarma_1@10.28.41.164:27017/')
'''
#=============================================
db = conn['StayOutletSummaries']
coll = db['StayOutletSummaries']

file = 'C:\PersonalProjects\PythonSnippets\Files\ATA.txt'
count = 0
for line in list(open(file)):
    print(coll.find_one({"StayId": int(line.strip())}))



#===========================================
db = conn['StaySummaries']
coll = db['StaySummaries']

file = 'C:\PersonalProjects\PythonSnippets\Files\ATA.txt'
count = 0
for line in list(open(file)):
    print(coll.find_one({"_id": int(line.strip())}))

'''
#================================================================
db = conn['SurveyInstances']
coll = db['SurveyInstances']

file = 'C:\PersonalProjects\PythonSnippets\Files\JE3_1.txt' #JGH.txt' #BDV.txt' #A360.txt'
count = 0
for line in list(open(file)):
    if str(coll.find_one({"_id": int(line.strip())})) != 'None':
        print(str(coll.find_one({"_id": int(line.strip())})))
#================================================================


'''
with open('C:\PersonalProjects\PythonSnippets\Files\ATA.csv','r') as csvfile:
    #line = csv.reader(csvfile, delimiter=' ')
    line = csv.DictReader(csvfile)
    for row in line:
        print(row)
        print(line.line_num)
'''

