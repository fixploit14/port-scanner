import socket
from common_ports import ports_and_services

ip_address = input("Enter IP address: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

socket.setdefaulttimeout(5)

print("-" * 40)
for port in range(start_port, end_port + 1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, port))
        service_name = ports_and_services.get(port, "Unknown")
        print(f"[+] Port {port} ({service_name}) is open")
        s.close()
    except (socket.timeout, ConnectionRefusedError):
        pass
print("-" * 40)
