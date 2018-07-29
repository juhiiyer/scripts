'''
GhitHub
https://github.com/ManoharPapasani123/Python
manohar.pc@gmail.com
Nested Functions
----------------
A function inside a function is called Nested Functions
'''

'''
example 1
def outer():
    print ('Outer functions')
    def inner():
        print ('inner functions')
    return inner

f1 = outer()
f1
'''

'''
example 2
def outer():
    def inner(a, b):
        print ('The sum is', a+b)
        print ('The product is', a*b)

    inner(1, 2)
    inner(10, 20)

outer()
'''
'''
Encapsulation
you use inner functions to protect them from everything happening
outside of the function, meaning they are hidden form the global
scope.
'''
'''

example 3

def outer(num1):
    def inner_increment(num1):
        return num1 + 1
    num2 = inner_increment(num1)
    print (num1, num2)

outer(10)
'''
'''
example 4

def div(f1):
    def div_check(a, b):
        if (b == 0):
            print ('denominator must not be 0')
        else:
            f1(a, b)
    return div_check


@div
def f1(a,b):
    print(a/b)

f1(10,0)
f1(23, 5)
'''

def decor1(func):
    def inner():
        x = func()
        return x*x
    return inner
def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@decor1
@decor
def f2():
    return 10

print (f2())
