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
