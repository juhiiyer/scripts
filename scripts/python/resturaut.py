#!/usr/bin/python3
print ('Welcome to my restaraunt, Little Bay.')
print ('I will be your servent who will serve you food on your door step.')
print ('By the way my name is Mr.Ghosh.')
print ('First thing on the list is the menue.')
print ('pizza(cheeese) = $20')
print ('pasta(red) = $15')
print ('lazania Extra Cheeeessyyy =  $23')
print ('garlic bread(with cheeese) = $10')
print ('POP corn(Extra cheeese) =  $25')
p_popcorn = int(25)
p_garlicbread = int(10)
p_lasagna = int(23)
p_pasta = int(15)
p_pizza = int(20)
total = 0
print('WARNING: type everything in lower case.')
print ('You can only have 2 items.')
firstitem = input('Item 1: ')
second_item = input('Item 2: ')

if firstitem == 'pizza':
    # print ('Your total is %s' %(p_pizza))
    total = total + p_pizza
elif firstitem == 'popcorn':
    # print ('Your total is %s' %(p_popcorn))
    total = total + p_popcorn
elif firstitem == 'garlic bread':
    # print ('Your total is %s' %(p_garlicbread))
    total = total + p_garlicbread
elif firstitem == 'lasagna':
    # print ('Your total is %s' %(p_lasagna))
    total = total + p_lasagna
elif firstitem == 'pasta':
    # print ('Your total is %s' %(p_pasta))
    total = total + p_pasta

if second_item == 'pizza':
    # print ('Your total is %s' %(p_pizza))
    total = total + p_pizza
elif second_item == 'popcorn':
    # print ('Your total is %s' %(p_popcorn))
    total = total + p_popcorn
elif second_item == 'garlic bread':
    # print ('Your total is %s' %(p_garlicbread))
    total = total + p_garlicbread
elif second_item == 'lasagna':
    # print ('Your total is %s' %(p_lasagna))
    total = total + p_lasagna
elif second_item == 'pasta':
    # print ('Your total is %s' %(p_pizza))
    total = total + p_pizza

print ('The sub total is %s' %(total))

tax = 0.08 * total

print ('The tax at 8 percent is %s' %(tax))

grand_total = total + tax

print ('The grand total is %s' %(grand_total))
