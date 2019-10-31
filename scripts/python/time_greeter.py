#!/usr/bin/python3.6
print('Welcome to the greeting centre')
question = int(input('What is the time(only type the hour): '))


try:

	value = int(question)
	print('Yes, it is an integer')

except ValueError:


	print('No, it is not an integer')

'''
print ('You have entered %s'%(question))
if type(question) == int:
	print ('Good')
else:
	print ('There is a preschool on the gachibowli chauraha. They might have free education for you.')
gm = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
'''