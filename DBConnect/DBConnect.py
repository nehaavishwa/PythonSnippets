import pypyodbc
import json as j
connection = pypyodbc.connect('Driver={SQL Server}; Server=NVSHWAKARMA7X64\\NEHAA; Database=TestDB; uid=sa;pwd=HelloWorld')
cursor = connection.cursor()

SQLCommand = ("SELECT TOP 10 Date ,Hour, [Requests], [Completes] FROM [TestDB].[dbo].[Analytics2] ")
cursor.execute(SQLCommand)
rows = cursor.fetchall()
x = list(map(lambda x: x[0], cursor.description))
l1 =[]
#print(cursor.description[0])
for l in cursor.description:
    #print(l[0])
    l1.append(l[0])
print(l1)
key_val_pair ={}# dict(rows[0])
#print(key_val_pair)
for row in rows:
    key_val_pair = {l1[0]: row[0], l1[1]: row[1], l1[2]:row[2], l1[3]:row[3]}
    #j.dump(key_val_pair, f)
    with open("Sql.json", 'w') as f:
        for k in key_val_pair:
            j.dump(k, f)
        f.write('\n')
    print(key_val_pair)

'''results = cursor.fetchone()
while results:
    print("Your customer " + str(results[0]) + " " + results[1] + " lives in " + results[2])
results = cursor.fetchone()
connection.close()
'''
