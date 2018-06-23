#!/usr/bin/python3.5
# this is just the countinuation of the guess_number.py. But in this, I am going to make a few 
#questions so that, if the person who is playing this game has already done his 10 chances, he could have another 5 chances 
# only if he answers my extremely difficult and random questions, he can have another 5 cahnces. If he dose not succeed even in 
# those 5 chances, then it is GAME OVER for him!
# Author = juhi s. Iyer and my father!

Q1 = input('What is the command in linux terminal to change the permissions of a file?: ')
ans1 = ('chmod')

if Q1 == ans1:
	print ('You are correct. You can get 5 more chances!')
else:
	print ('You are wrong. The correct answer was chmod. So, for you, it is GAME OVER!')

Q2 = input('Name a secure way to login from one computer to another?: ')
ans2 = ('ssh (secure shell)')

if Q2 == ans2:
	print ('You are correct. You can get 5 more chances!')
else:
    print ('You are wrong. The correct answer is ssh (secure shell).So, for you it is GAME OVER!')

Q3 = input('Name an inecure protocal to log into a compter?: ')
ans3 = ('telnet')

if Q3 == ans3:
	print ('You are correct. You can get 5 more chances!')
else:
    print ('You are wrong! The correct answer is Telnet! You cannot go forward. So, it is GAME OVER!')

Q4 = input('What is the port number for ssh?: ')
ans4 = ('22')

if Q4 = ans4:
	print ('You are correct. You have 5 more chances to go!')
else:
    print ('You are wrong. The correct answer is 22. So, for you it means GAME OVER!')

Q5 = input('Which file contains the DNS server inoformation?: ')
ans5 = ('/etc/resolv.conf')

if Q5 == ans5:
    print ('You are correct. You can try to get the answer in 5 more chances!')
else:
    print ('You are wrong. The correct answer is /etc/resolv.conf. So, for you itis GAME OVER!')     	
