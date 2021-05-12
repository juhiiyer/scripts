#!/usr/bin/env python3
import portscanner

targets_ip = input('Enter the required target to scan for vulnerable open ports: ')
port_number = int(input('Enter the number of ports you want to scan: '))
vul_file = input('Enter the path of the file with the vulnerable software: ')
print('\n')

portscanner.scan(targets_ip)