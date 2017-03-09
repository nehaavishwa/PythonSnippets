# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 07:45:15 2017

@author: nvishwakarma
"""

import re
#import csv
#import pandas as p

filePath = r'C:\Users\nVishwakarma\Documents\SQL Server Management Studio\Projects\UnusedObject\Trans_Invalid.txt'
s_proc=set()

with open(filePath, 'r') as f:
        for line in f:
            search = re.search(r'Procedure.*[,]',line)
            search1 = re.search(r'module ''.*depends \'',line)
            s_proc.add(search.group().split('&amp;'))
            print(s_proc)