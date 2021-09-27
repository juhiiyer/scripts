import socket
from IPy import IP

def scan(target):
    converted_ip = check_ip(target)
    print('\n' + 'Scanning target : ' + str(target))
    for port in range(79,82):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        print('[+] Port ' + str(port) + ' is open')
    except:
        pass


targets = input('[+] Please Enter the Required target/s (split many targets with comma): ')

if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))
else:
    scan(targets)

