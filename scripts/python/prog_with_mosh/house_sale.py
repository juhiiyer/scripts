#!/usr/bin/python3.7
price_of_house = 1000000
credit_good = True
ten_per_price = 1000000*10/100
twenty_per_price = 1000000*20/100
if credit_good:
    print('You only have to pay 10per i.e $%s'%(ten_per_price))
else:
    print("You have to pay 20per i.e $%s"%(twenty_per_price))