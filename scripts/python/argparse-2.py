#!/usr/bin/python3.5
import argparse

parser = argparse.ArgumentParser(description = 'To show them their salary per week!')
parser.add_argument('-n', '--name', required = True, help = 'Your name please')
parser.add_argument('-a', '--amount', type = int ,required = True, help = 'Your amount of money please')

args = parser.parse_args()
name = args.name
amount = args.amount

print ('Your name is {}.'.format(name))
print ('Hi {}, your salary per week is ${}.'.format(name, amount))

total = 100 + amount 

print ('So then, your salary and tax together make an amount which is {} per week.'.format(total))