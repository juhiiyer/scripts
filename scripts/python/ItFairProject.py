#!/usr/bin/python3.5
'''
This is a guess the number game. In this, we habve to guess a number in only 10 tries. I hope you will enjoy this game!
Author = Juhi Seshadri Iyer
'''

from random import randint
from random import shuffle

import sys

print ('This is a games, in which you ohave to guess a number. If you guessed the number below 10 tries, you will get a suprise')

print ('INSTRUCTION!')
print ('- You have to guess a random number that the computer has chosen.')
print ('- Then you would have to guess that number in only 10 tries')
print ('- Then, you can play a suprise game!')
print ('- Well, it is your choice if you want to play the game.')
print ('- The game will automaticly pop out, after you are done!')

def number_game():

    x = randint(1,100)
    

    print('I have chosen a number between 1 and 100. Try and guess the number')

    tries = 0
    max_tries = 10

    while tries < max_tries:
        guess = int(input("Guess: "))
        
        if guess > 100 or guess < 1:
            print('The number that you entered is not between 1 and 100')
            sys.exit()


        if guess == x:
            print('Correct you found the answer in %s tries'%(tries + 1))
            response = input('do you want to play my other game called the linux game? say y/n: ')
            if response == 'y':
                linux_game()
            else:
                print ('Thank you for playing my game. I hope you enjoyed it!')
                sys.exit()

        elif abs(guess - x) > 10:
            print('Cold')
        elif abs(guess - x) > 5 and abs(guess -x) < 10:
            print('Almost there')
        elif abs(guess -x) < 5:
            print('Extremely close')
        tries = tries + 1
        if tries == max_tries:
           print ('You are wrong. All of your chances are over!')
           print ('The random number that I chose was %s'%(x))
           print ('Its time that your chance goes for a toss! Mwa ha ha ha!')

def sample_question():
    print ('These are some sample questions. Do not remember the answer, as these questions are just a sample!')
    
    Q = input('How to go temperalily root?: ')
    A = ('sudo')
    if Q == A:
        print ('You are correct! WOW!')
    else:
        print ('You are wrong. The correct answer is sudo. So, it is GAME OVER!')
        sys.exit()

    Q01 = input('Which linux distribution does the cyber security people use?: ')
    A01 = ('kali linux')

    if Q01 == A01:
        print ('You are correct! You are the one with the sixth sense! You are surely one of kind. So I hope you enjoyed my game! Thank you and have a great day!')
    else:
        print ('You are wrong. The correct answer is kali linux. So it is GAME OVER!')
        sys.exit()
            



def linux_game():

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

        Q3 = input('Name an insecure protocol to log into a computer?: ')
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


number_game()
sample_question()
#linux_game()
