#!/usr/bin/python3.5
'''
else clause:
    It is used to write a more readible code
    It is an optional block
'''
import sys

try:
    fp = open('/tmp/integers.txt','r')

except IOError as e:
    # print ('NO SUCH FILE')
    print (e.args)
    # sys.exit()
else:
    data = fp.readlines()
    print (data)
    #print ('Hello')
finally:
    fp.close()
    #print ('File closed')