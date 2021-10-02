import portscanner

targets_ip = input('[+] * Enter target to scan for vulnerable open ports *: ')
port_number = int(input('[+] Enter the number of ports you want to scan (500 means first 500 ports): '))
vul_file = input('[+] Enter the path to the file of the vul software: ')
print('\n')

target = portscanner.PortScan(targets_ip, port_number)
target.scan()

with open(vul_file ,'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print('[!!] VULNERABLE BANNER: "' + banner + '" ON PORT: ' + str(target.open_ports[count]))
        count += 1
