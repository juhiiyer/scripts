#!/usr/bin/python3
print('Welcome to my restaraunt, Little Bay.')
print('I will be your servent who will serve you food on your door step.')
print('By the way my name is Mr.Ghosh.')
print('First thing on the list is the menue.')
print('pizza(cheeese) = $20')
print('pasta(red) = $15')
print('lasagna(Extra Cheeeessyyy) =  $23')
print('garlic bread(with cheeese) = $10')
print('POP corn(Extra cheeese) =  $25')
p_popcorn = 25
p_garlicbread = 10
p_lasagna = 23
p_pasta = 15
p_pizza = 20
total = 0

print (p_pasta)

print('WARNING: type everything in lower case.')
print('You can only have 1 items.')
firstitem = input('Item 1: ')


if firstitem == 'pizza':
    price = 20
    total += price

if firstitem == 'popcorn':
    price = 25
    total += price

if firstitem == 'garlicbread':
    price = 10
    total += price

if firstitem == 'lasagna':
    price = 23
    total += price

if firstitem == 'pasta':
    price = 15
    total += price





print('Your total is %s'%(total))



'''

if firstitem == 'pizza' or 'pasta' or 'lasagna' or 'popcorn' or 'garlic bread':
    total = int('p_' + firstitem)
    print('Your total bill with taxes is %s'%(total))
    print('Thank you for ordering from our shop and bye.')
else:
    print('I think there is a mistake in your input. Please follow the instructions and run the program again')

'''




    