#!/usr/bin/env python3
import socket
from IPy import IP


def scan(targets):
    converted_ip = check_ip(targets)
    print(' \n' + ' Scanning the target ' + str(targets))
    for port in range(lport, mport):
        portscan(converted_ip, port)


def check_ip(ip):
    ''' this function will convert the domain name into an ip address.'''
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return(socket.gethostbyname(ip))

def get_banner(s):
    return s.recv(1024)



def portscan(ipaddress, port):

    try:


        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('(+) The port ' + str(port) +' is open. : ' + str(banner.decode().strip('\n')))
        except:
            print( '(+) The port ' + str(port) +' is open.' )

    except:

        pass

if __name__ == '__main__':
    
    targets = input('(+) enter the target/s ip address (separate targets with ",") : ')
    lport = int(input('(+) enter the minimum port number: '))
    mport = int(input('(+) enter the maximum port number: '))

    if ',' in targets:

        for ip_add in targets.split(','):

            scan(ip_add.strip(' '))

    else:

        scan(targets)
