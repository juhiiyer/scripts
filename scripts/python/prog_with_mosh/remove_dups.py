#!/usr/bin/python3.7

'''
This program removes duplicate items in a list
Author: Juhi S Iyer 
Date: 10 Jan 2020
'''

MYLIST = ['aa', 'bb', 'cc', 'dd', 'aa', 'ee']
NEWLIST = []

for item in MYLIST:
    if item not in NEWLIST:
        NEWLIST.append(item)
print(NEWLIST)