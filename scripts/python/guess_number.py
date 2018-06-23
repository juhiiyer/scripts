#!/usr/bin/python3.5
'''
This is a guess the number game. In this, we habve to guess a number in only 10 tries. I hope you will enjoy this game!
Author = Juhi Seshadri Iyer
'''

from random import randint
import sys

x = randint(1,100)
print ('The random number that I chose was %s'%(x))

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
        sys.exit()

    elif abs(guess - x) > 10:
        print('Cold')
    elif abs(guess - x) > 5 and abs(guess -x) < 10:
        print('Almost there')
    elif abs(guess -x) < 5:
        print('Extremely close')
    tries = tries + 1
    if tries == max_tries:
       print ('Its time that your chance goes for a toss! Mwa ha ha ha!')
    #     print ('If you answer all of my question correctly, then you will have 5 more chances.')

    #     Q1 = print (input('Q1: What is the command to change permissions in linux terminal?: '))
    #     answer_1 = 'chmod'
    # if answer_1 == Q1:
    #      print ('You are correct. you get 5 more chances!')
    #       min_tries = 5
    # if min_tries == 5:
       print ('I am sorry, but you have lost your chances.')
       print ('So, GAME OVER!')

    
              





    


