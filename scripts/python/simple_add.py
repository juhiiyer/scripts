''' This is a program to show addition
and multiplication
Author: Juhi S Iyer 21 Oct 2017
'''

A = 2
B = 3
C = A * B
D = A + (B * C)
# print ('%s x %s = %s'%(a, b, c))
print 'the product of %s and %s is %s!!!!!wwooww. '%(A, B, C)
print 'the math thingi of %s and %s is %s and %s? '%(A, B, C, D)

def AddMe(num1, num2):
	''' This function will print the sum of two numbers
	'''
	SUM = num1 + num2
	print 'The sum of {} and {} is {}'.format(num1, num2, SUM)


def multiplyme(no1, no2):
	'''the same thing written on the top exept i am going to multiply
	'''
	PRODUCT = no1 * no2
	print 'the sum of {} and {} is {}'.format(no1, no2, PRODUCT)

multiplyme(787,9765)
AddMe(4, 7)