#!/usr/bin/python3.7
'''
this program converts numbers into words:
ex:123
output: one two three
'''
NUMBER = input('Type the number: ')
VALUES = {
    "1" : 'One',
    "2" :'Two',
    "3" : 'Three',
    "4" : 'Four',
    "5" : "Five",
    "6" : 'Six',
    "7" : 'Seven',
    "8" : 'Eight',
    "9" : 'Nine',
    "0" : 'Zero'
}

NUM_LEN = len(NUMBER)
for i in NUMBER:
    if i in VALUES:
        print(VALUES[i])
    NUM_LEN = NUM_LEN - 1
