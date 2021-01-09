#!/usr/bin/python3.5
import re
text = 'Google Chapter 22 - The Production Environment at 456 Apple'
string = 'oog'
if re.match(string, text):
    print('found')
