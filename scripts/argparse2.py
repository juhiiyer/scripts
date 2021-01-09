#!/usr/bin/python
'''
This will take 2 args and add and multiply them.
'''
import argparse

DISCRPTION = argparse.ArgumentParser(description='Script to add and multiply 2 numbers.')
DISCRPTION.add_argument('-a', '--num1',
                        help='the first number',
                        required='True',
                        default='2')

DISCRPTION.add_argument('-b', '--num2',
                        help='The second number',
                        required='True',
                        default='3')
RESULTS = DISCRPTION.parse_args()

def sum_of_numbers(num1, num2):
    '''
    This function adds two numbers
    '''
    sum_of = int(num1) +  int(num2)
    return sum_of

def product_of_numbers(num1, num2):
    '''
    This function multiplies two numbers
    '''
    prod_of = int(num1) * int(num2)
    return prod_of

print 'SUM = %s'  %(sum_of_numbers(RESULTS.num1, RESULTS.num2))
print 'PRODUCT = %s' %(product_of_numbers(RESULTS.num1, RESULTS.num2))
