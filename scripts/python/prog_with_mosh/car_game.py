#!/usr/bin/python3.7
user_input = ""


while True:

    user_input = input('> ').lower()

    if user_input == 'help':
        print(' Start: The car will start. \n Stop: The car will stop. \n Quit: It will quit the game.')
        # break
    elif user_input == 'start':
        print('Car started............... READY TO GOOOOOOOOOOOOOOOOOOOOOOOOOOOO!')
        # break
    elif user_input == "stop":
        print('Car stpped.')
        # break
    elif user_input == 'quit':
        print('Qitting..................')        
        break
    else:
        print('Invalid input')
    
