#!/usr/bin/env python


import argparse


parser = argparse.ArgumentParser(description = 'Greet a person')
parser.add_argument('-n', '--name', required = True, help='Your firstname')
parser.add_argument('-l', '--last', required = True, help='Your lastname')
parser.add_argument('-c', '--city', required = True)
parser.add_argument('-p', '--pincode', type=int, required = True, help='Your pincode')


args = parser.parse_args()
name = args.name
last = args.last
city = args.city
pincode = args.pincode	


print ('hello {} {}'.format(name, last))
print ('You live in {}'.format(city))
print ('Your pin code is {}'.format(pincode))