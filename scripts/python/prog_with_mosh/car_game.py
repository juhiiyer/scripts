#!/usr/bin/python3.7
user_input = ""
started = False
stopped = False

while True:

    user_input = input('> ').lower()

    if user_input == 'help':
        print(' Start: The car will start. \n Stop: The car will stop. \n Quit: It will quit the game.')
        break 
    if user_input == "start":
        if started:
            print('Already started!')
        else:
            started = True
            if stopped == True:
                print('Car started!')

    elif user_input == "stop":
        if stopped:
            print('Car already stopped.')
        else:
            stopped = True
            print('Car stopped.')    
    elif user_input == 'quit':
        print('Quitting..................')        
        break
    else:
        print('Invalid input')
    
