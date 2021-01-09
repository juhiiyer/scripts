'''
suppose you have developed a very large application that includes many
modules. As the number of modules grow, it becomes difficult to keep track
of all of them if they are dumped into one location.

packages
---------
A package is a colection of modules.

functions/modules/packges are used to build modular code.
a package is reusable
a package avoids naming conflict.

python 3.3 version using_inint_.py is neccasery. In lattest versions,
it is not mandotary.

Directory
  __init__.py
  module1.py
  module2.py

By deafault the folder in which we place .py files is a  package

datascience
  module.py
  shapes.py

import packages
---------------

we can import in 3 ways
1) Normal import

2) from... import ....

3) form .... import *

Aliasing
--------

Normal import
--------------

syntax
--------
import packagename.module1 as alias1, packagename.module1 as alias1, ...

'''

import random
print (dir(random))

help(random.__spec__)
dashes = "-------------------"
    
print (dashes)



import sys
print(sys.path)

sys.path.append('/tmp/foo')

print(sys.path)

sys.path.append('/tmp/foo/bar')


'''
importing multiple packages
random numbers
rm.py


'''


'''
regular expressions

i tus used to implement pattern matching.

the python module name is re (e.g. import re)

define a regex using the syntax:

r'expression'

ex: r'ab*c'

ex:

import re
regex=r'ab*c'
matches=re.findall(regex,'ac,abc,abbc,abbbc')
print(matches)

ex 1:

ab*c  ->> zero or more occurrences of b. valid patterns are abc,
abbc, ac (zero b's)

ex 2:



it matches with one or more occurrences of preceding character

1. *----> It matches 0 or more occurences'''
import re
s = "geeks for geeks geer get the boot boor geem booat aap bool aab aaat boot1 boomb"

regex1=r'gee'
regex2=r'boo'
regex3=r'aa'

matches1 = re.findall(regex1,s)
matches2 = re.findall(regex2,s)
matches3 = re.findall(regex3,s)
print (matches1)
print (matches2)
print (matches3)

l1 = len(matches1)
l2 = len(matches2)
l3 = len(matches3)

print(l1, l2, l3)
s
geekdict = {}
for i in range(1,4):
    print (i)
    geekdict['matches%s'%i] = 'l%s'%i

print(geekdict)
    

