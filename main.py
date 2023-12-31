# Port Scanner
# Created by fixploit14

import socket

ip_address = input("Enter IP address: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

socket.setdefaulttimeout(5)

print("-" * 40)
for port in range(start_port, end_port + 1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, port))
        print(f"[+] Port {port} is open")
        s.close()
    except (socket.timeout, ConnectionRefusedError):
        pass
print("-" * 40)
