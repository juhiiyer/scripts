#!/usr/bin/env python3
import socket
from IPy import IP

lport = 20
mport = 25

class PortScan():
    banners = []
    open_ports = []
    def __init__(self, target, port_num):
        self.target = target
        self.port_num = port_num


    def scan(self):
        for port in range(lport, mport):
            self.scan_port(port)


    def check_ip(self):
        ''' this function will convert the domain name into an ip address.'''
        try:
            IP(self.target)
            return(self.target)
        except ValueError:
            return(socket.gethostbyname(self.target))        



    def scan_port(self, port):

        try:

            converted_ip = self.check_ip()
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((converted_ip, port))
            self.open_ports.append(port)
            try:
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                self.banners.append(banner)
                
            except:
                self.banners.append(' ')
            sock.close()    

        except:

            pass


