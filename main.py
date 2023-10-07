# Port Scanner
# Created by fixploit14

import socket

text="Port Scanner"

print("-" * 35)
print(f"{text:^35}")
print("-" * 35)

ip_address = input("Enter IP address: ")
port_range = input("Enter the range of ports, separated by a hyphen (e.g., 80-443): ").split('-')
port_start = int(port_range[0])
port_end = int(port_range[1])

socket.setdefaulttimeout(5)

print("-" * 35)
for port in range(port_start, port_end + 1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, port))
        print(f"[+] Port {port} is open")
        s.close()
    except (socket.timeout, ConnectionRefusedError):
        pass
print("-" * 35)
