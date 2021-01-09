#!/usr/bin/python3.5

class InsufficientFundsError(Exception):
    pass

balance = float (input('enter balance: '))
amount = float (input('enter amount:'))

while True:
    amount = float(input('enter amount'))
    if (amount > balance):
        try:
            raise InsufficientFundsError('Funds are not sufficient.')
        except InsufficientFundsError as e:
            print (e)
            print('enter amount less than balance')
    else:
        print ('transection seccess!')
        break