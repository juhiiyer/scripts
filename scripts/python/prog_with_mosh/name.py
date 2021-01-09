#!/usr/bin/python3.7
name_length = len(input('Enter your name: '))
if name_length < 3 or name_length > 50:
    print('No one can have such a abnormal name')
# elif name_length > 50:
    # print('No one can have such a loooooong name!')
else:
    print('Doog! Noice name!')