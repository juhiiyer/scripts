import argparse

parser = argparse.ArgumentParser(description='A test argument parser')
parser.add_argument('-f', '--first_number', type=int, help='enter first number')
second_parser = argparse.ArgumentParser(description = 'A second argument paresr')
parser.add_argument('-s', '--second_number', type = int, help = 'enter second number')



parameters = parser.parse_args()

first_no = parameters.first_number
second_no = parameters.second_number
third_number = first_no + second_no


print ('You entered the first number: {}'.format(first_no))
print ('You entered the second number: {}'.format(second_no))
print (third_number)
