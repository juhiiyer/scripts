'''

# example 1


class Counter:
    x = 10

    def incr(self):
        Counter.x = Counter.x + 1

        print (Counter.x)

c1 = Counter()
c2 = Counter()
c3 = Counter()

c1.incr()
c2.incr()
c3.incr()
c2.incr()
'''
'''
a static function is declered using decorator.
a static method is not part of the object. it is part
of the class.

not to use self for static methods.

how to call a static function

ClassName.function_name()



'''

'''
class Counter:
    x = 10
    def init(self):
        self.a = 20
    
    @staticmethod
    def incr():
        Counter.x = Counter.x + 1
        print (Counter.x)
        c = Counter()
        c.init()
        print(c.a)



Counter.incr()

'''

'''
we can acces static variables from instance functions directly.
A staticmethod allows to acess only static members (variables,functions)
directly but if we want to access instnace members(variables/functions),
from a static function, the nwe should create the object of a
class in a static method and we must acess the instance members
using reference of object or object itself.



classmethod
===========

It is similar to static function,
but declared using the decorator
@classmethod

A classmethid is declered with a parameter cls

syntax
======
@classmethod

def function_name(cls):
    statements

How to cal class function
========================

ClassName.function_name()


'''
        
'''
    
class Counter:
    x = 10
    def init(self):
        self.a = 20
    
    @classmethod
    def incr(cls):
        Counter.x = Counter.x + 1
        print (Counter.x)
        c = Counter()
        c.init()
        print(c.a)



Counter.incr()
'''
'''regex1.py
instance var vs static var

a static var can be called by all the instances of the class,
but a static var can be called by only the function
in which is it defined.



types of variables:
===================
global,local.static/class,instance

types of functions:
==================

normal (outside class)
instance (inside class)
static(inside class)
class(inside class)

a Constructor is a special function used to decare and initiase
instance variables of a class.
A contructor is automatically called whenever on object is created.

Remember that we have to call the functions in a class. A constructor
need not be called.

syntax:
======
def __init__(self):
    statements




# example 3

class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price


    def display(self):
        print (self.name)
        print (self.author)
        print (self.price)
    
Reference = Book('aa', 'bb', 50)
Reference.display()

# -------------------------------
a destructor is used to perform garbage collection
garbage collection is the process of rmoving unwanted objects
from memory
it happens automatically in python
a destructor is automatically called once after the program
completes execution

garbage collection can be done implicitly or explicitly
by calling del referencename

'''

class A:
    def __del__(self):
        print ('Object destroyed')

a1 = A()
a2 = A()
a3 = A()
a4 = A()
a5 = A()

del a1
del a4

# print ('The end')


