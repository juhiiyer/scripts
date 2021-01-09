'''
OOP:

Object
Class
Encapsulation
Abstractction
Inheritance
Polymorphiesum
Message passing
Dynamic binding

Object: It is a real-world entity like person, place, thing.

Class: A class describes properties and actions about an object

It contains variables and functions.

It is a plan (blueprint) of an abject.

We declare a class using keyword "class".

we use variables to declare properties.
we use functions to declare actions.

SYNTAX
======

referenceName=ClassName()

class
=====

describes an object

A class is a collection of variables and functions.

Syntax to describe a class:


class ClassName:
    variables
    functions/methods

steps to implement classes and objects

A function inside a class is called a method

step1: define a class:

class Pizza:
    //

step2: create an object using referenceName=ClassName()

p = Pizza()

step 3: accessing members of a class

p.flavour (if flavour is a variable)
p.taste() (if taste is a function)

how to call members inside a class
==================================


self.varname
self.function_name()


if oyu are defining a function inside a class, you have to
have "self" as the argument. e.g:

def function_name(self, var1, var2):
    ...
    ...

How to define instance members in python:
========================================

- declare any instance member using "self" keyword




'''
'''
example 7


class Pizza:
    def init(self, name, price, flavour):
        
        self.name = name
        self.price = price
        self.flavour = flavour

    def display(self):
        print (self.name)
        print (self.price)
        print (self.flavour)


p = Pizza()
p.init('margerita', '400.00', 'paneer')
p.display()
'''
'''

whenever an object is created, it is allocated a unique address.
the ddress is initialized ot a vaiable called the refernence variable.
variables in side objects are called instance variabls.
instance variables are decleared inside a functin iusing keyword self.
a function decleraed using inside lass using keyword self
as parameter are called instance functions
instance fucntions operate on objects


'''

'''
a = 10

class A:
    a = 20
    def f1(self):
        self.a = 30
        a = 40
        print (a)
        print (self.a)
        print (A.a)
        print (globals()['a'])

print (a)

a1 = A()
a1.f1()
'''
class Addition:
    m = 500
    def init(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        self.c = self.a + self.b


    def display(self):
        print ('The sum of %s and %s is %s'%(self.a, self.b, self.c))
        # print ('The value of (a + b) times m is %s' %(self.c * m)) 

X = Addition()

X.init(3,4)
X.add()
X.display()
print (X.m)

'''

static variables and functions
=============================

a variable defined inside a class but outside a function is called a static
 or class variable. a static variable is accessed directly using the class name
like ClassName.StaticVarName

'''

        



















