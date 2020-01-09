#!/usr/bin/python3.7

'''
 this program finds the largest number and prints it out for you.
'''
NUMBERS = [1, 12, 663, 44, 25, 68, 733, 8777, 29]


MAX_NUM = 0
for number in NUMBERS:
    if number >= MAX_NUM:
        MAX_NUM = number

print('The largest number is {}'.format(MAX_NUM))
