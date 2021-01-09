#!/usr/bin/python3.5

'''
this is just the countinuation of the guess_number.py. But in this, I am going to make a few 
questions so that, he can have 5 cahnces. If he dose not succeed even in 
those 5 chances, then it is GAME OVER for him!
Author = juhi s. Iyer

'''

import sys
from random import shuffle

def q1():

	Q1 = input('What is the command in linux terminal to change the permissions of a file?: ')
	ans1 = ('chmod')

	if Q1 == ans1:
		print ('You are correct!')
	else:
		print ('You are wrong. The correct answer was chmod. So, for you, it is GAME OVER!')
		sys.exit()

def q2():

	Q2 = input('Name a secure way to login from one computer to another?: ')
	ans2 = ('ssh')

	if Q2 == ans2:
		print ('You are correct!')
	else:
	    print ('You are wrong. The correct answer is ssh (secure shell).So, for you it is GAME OVER!')
	    sys.exit()

def q3():

	Q3 = input('Name an inecure protocal to log into a compter?: ')
	ans3 = ('telnet')

	if Q3 == ans3:
		print ('You are correct!')
	else:
	    print ('You are wrong! The correct answer is Telnet! You cannot go forward. So, it is GAME OVER!')
	    sys.exit()

def q4():

	Q4 = input('What is the port number for ssh?: ')
	ans4 = ('22')

	if Q4 == ans4:
		print ('You are correct!')
	else:
	    print ('You are wrong. The correct answer is 22. So, for you it means GAME OVER!')
	    sys.exit()

def q5():

	Q5 = input('Which file contains the DNS server inoformation?: ')
	ans5 = ('/etc/resolv.conf')

	if Q5 == ans5:
	    print ('You are correct!')
	else:
	    print ('You are wrong. The correct answer is /etc/resolv.conf. So, for you itis GAME OVER!')     	
	    sys.exit()

questions = [q1, q2, q3, q4, q5]
shuffle(questions)

for question in questions:
	question()
