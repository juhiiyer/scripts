#!/usr/bin/python3
print('Welcome to my restaraunt, Little Bay.')
print('I will be your servent who will serve you food on your door step.')
print('By the way my name is Mr.Ghosh.')
print('First thing on the list is the menue.')
print('pizza(cheeese) = $20')
print('pasta(red) = $15')
print('lazania(Extra Cheeeessyyy) =  $23')
print('garlic bread(with cheeese) = $10')
print('POP corn(Extra cheeese) =  $25')
popcorn = int(25)
garlicbread = int(10)
lazania = int(23)
pasta = int(15)
pizza = int(20)
print('WARNING: type everything in lower case.')
print('You can only have 1 items.')
firstitem = input('Item 1: ')

if firstitem == 'pizza' or 'pasta' or 'lazania' or 'popcorn' or 'garlic bread':
	total = firstitem + int(8)
	print('Your total bill with taxes is %s'%(total))
	print('Thank you for ordering from our shop and bye.')
else:
	print('I think there is a mistake in your input. Please follow the instructions and run the program again')






    