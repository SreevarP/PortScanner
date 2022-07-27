import socket
import time

class PortScanner:
    
    def __init__(self, ADDRS, port_range):
        self.ADDRS = ADDRS
        self.port_range = port_range
        self._scanPorts(ADDRS, port_range)
        
    def _scanPorts(self, ADDRS, port_range):
        
        open_ports = []
        
        if port_range is 'max':
            port_range = [1, 65355]
        if port_range is 'min':
            port_range = [1, 50]
        else:
            port_range = port_range.split('-')
            
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.results = {i: s.connect_ex((ADDRS, i)) for i in range(int(port_range[0]), int(port_range[1]))}
        
        for i, result in enumerate(self.results.items()):
            if result[1] == 0:
                print(f"\n Port {result[0]} is open")
                open_ports.append(result)
        
        if len(open_ports) == 0:
            print(f"\n {ADDRS} does not have any open ports in that range")

print(r'''   _____                                 _____      _   _                       
  / ____|                               |  __ \    | | (_)                      
 | (___  _ __ ___  _____   ____ _ _ __  | |__) |_ _| |_ _ _   _  __ _ _ __ __ _ 
  \___ \| '__/ _ \/ _ \ \ / / _` | '__| |  ___/ _` | __| | | | |/ _` | '__/ _` |
  ____) | | |  __/  __/\ V / (_| | |    | |  | (_| | |_| | |_| | (_| | | | (_| |
 |_____/|_|  \___|\___| \_/ \__,_|_|    |_|   \__,_|\__|_|\__, |\__,_|_|  \__,_|
                                                           __/ |                
                                                          |___/                 ''')
print('\n********************************************************************************')
print("\n* Copyright of Sreevar Patiyara, 2022")
print('\n* Github: https://github.com/SreevarP')
print('\n* Email: sreevarpatiyara@gmail.com')
print(r'''  ____            _   ____                                  
 |  _ \ ___  _ __| |_/ ___|  ___ __ _ _ __  _ __   ___ _ __ 
 | |_) / _ \| '__| __\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 |  __/ (_) | |  | |_ ___) | (_| (_| | | | | | | |  __/ |   
 |_|   \___/|_|   \__|____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                            ''')
print('\n Version 1.0')
print('\n********************************************************************************')
HOST = input('\n Please enter an IPv4 address: ')
port_range = input("""\n Please enter the port range you wish to scan. Port range must use '-', i.e 50-100. 
Enter 'max' if you wish to scan all ports and 'min' to scan the set minimum amount of ports: """)
if __name__ == '__main__':
    PortScanner(HOST, port_range)