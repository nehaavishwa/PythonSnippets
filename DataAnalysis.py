__author__ = 'nvishwakarma'

import json

path = r'C:\PersonalProjects\PythonSnippets\Files\usagov.txt'
records = [json.loads(line) for line in open(path)]


def reccounting():

    #print(records[0]['tz'])
################Counting Time Zones in Pure Python
    time_zones = [rec['tz'] for rec in records if 'tz' in rec]
    return time_zones[:10]
    #print(time_zones[:10])


def get_counts(seq):
    counts = {}
    for x in seq:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts


def top_count(count_dict, n):
    key_val_pair = [(count, tz) for tz, count in count_dict.items()]
    key_val_pair.sort()
    return key_val_pair[-n:]




#time_zone = reccounting()
#print(time_zone)
time_zone = [rec['tz'] for rec in records if 'tz' in rec]
print(time_zone[:10])
count = get_counts(time_zone)
print(count['America/New_York'])
print(len(time_zone))
print(top_count(count, 5))

