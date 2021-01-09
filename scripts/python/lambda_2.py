'''
Lambda:
Functions are also objects




'''

def f1(a, b):
    c = a + b
    return c
print(f1(23, 45))


x = lambda a, b:a * b


print (x(21, 345))

x = lambda a, b, c: a if a>b and a>c else b if b>c else c
    
print (x(10, 10, 20))


x = [1, 2, 3, 4, 5]
a = 0
for i in x:
    x[a] = i + 100
    a = a + 1
print (x)
# Filter ex:
x = [1, 2, 3, 4, 5]
a = 0
for i in x:
    #x[a] = i + 100
    if i>3:
        print (i)
    #a = a + 1


# Reudce example

x = [1, 2, 3, 4, 5]
sum = 0
for i in x:
    sum = sum + i
    
print (sum)

'''
filter()
we can use filter function to filter values from the given sequence.
useful to deal with large data sets.
'''
m = 6

def isOdd(x):
    if (x%2==1):
        return True
    else:
        return False

l = [1,2,3,4,5]

x = list(filter(isOdd,l))

print ('example 6')

l = [0,5,10,15,20,25,30]
l1 = list(filter(lambda x:x%2 == 0,l))
print (l1)

'''
if we want to iterate every element in a sequence of
data and apply some functionality then python offers a function
called map().'''

print ('juhi thinks she is great, but she is actually great')

l = [1, 2, 3, 4, 5]
l2 = [1,8,7,6,2]

def sumlist(x):
    return 100 + x
l1 = list(map(sumlist,l))

print (l1)

l1 = list(map(lambda x,y:x*y, l,l2))
print (l1)
'''
we can apply map functions on top of multiple lists but make sure
all lists have same length
'''
'''
reduce function()
it is used to sequence of elements into a single by applying the
specified function!
'''
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [7, 7, 7, 7, 7 ,7 ,7 ,7, 7, 7]

table = list(map(lambda x,y:x*y, x,y))
print (table)


'''
reduce() is available in present in module called functools modules
and which should writ eimport statement
'''

from functools import *
x = [1, 2, 3, 4, 5]
sum = 0
def add(a, b):
    print (a, b)
    c = a + b
    a = b
    b = c
    return c
l = reduce(add,x)
print (l)
print('aadaaing')

from functools import *
l1 = [1, 2, 3, 4, 5]
l3 = reduce(lambda x, y:x*y,range(1,10))
print (l3)

dashes = '------------------'
print(dashes)
print('function aliasing')



'''
for an existing function we can give another name which is nothin but
function aliasing
'''

def f1(name):
    print ('hello',name)

f2 = f1
print (id(f1))
print (id(f2))

f1('chukchuk')
f2('tickbook')


'''
we can use the function by calling either f1 or f2.
in the above function if we delete one, the other works
'''

print(dashes)

'''
decorators
'''

'''
functioin decorater
-------------------
decorater is a function which can take a function as an argument.
'''
'''
modules
-------
a module is a file containing Python definations and statements
'''
def decor(func):
    def inner(name):
        if name == 'juhi':
            print ('hello juhi, today it is raining unicorns and mermaids.')
        else:
            fun(name)
    return inner
@decor
def f1(name):
    print ('hello',name, 'good morning')
f1('juhi')
f2('manu')

print(dashes)
import random
print (dir(random))
print (dashes)

'''
a module is a collection of
- functions
- variables
- classes
definitions from a module can be imported into other modules
into th emain module

the file name is the odule name wiht th esuffix .py appended

within a module, the modules' name (as a string) is available as the
value of the global variable __name__.
The program itself in python is a module.
'''

import sys
print (dashes)



'''
modules are helpful because:

reusable
readablility

Import statement:
We can use any pyhton source file as a module by excucuting an
import statement in some other python source file.

-When interpritter encounters an import statement, it imports a
module if the module is present in the search path.

- for example;
to import the module module.py, we need to put the following
command at the top of the script.



'''
import math, os, sys
import fibonacci

y =fibonacci.fib2(10)


print(y)

