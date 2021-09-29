import socket, sys
from IPy import IP


def scan(target):
    converted_ip = check_ip(target)
    print('\n' + 'Scanning target : ' + str(target))
    for port in range(79,81):
        scan_port(converted_ip, port)


def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)


def get_banner(s):
    return s.recv(1024)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open port ' + str(port))
    except:
        pass

if __name__ == "__main__":
    targets = input('[+] Please Enter the Required target/s (split many targets with comma): ')
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)

