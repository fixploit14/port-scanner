# portscanner 
# dibuat oleh fixploit14

import socket

alamat_ip = input("Masukkan alamat IP: ")
port_range = input("Masukkan rentang port awal dan akhir yang dipisahkan dengan tanda strip (contoh: 80-443): ").split('-')
port_start = int(port_range[0])
port_end = int(port_range[1])

socket.setdefaulttimeout(5)

print("-"*35)
for port in range(port_start, port_end + 1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((alamat_ip, port))
        print(f"[+] Port {port} terbuka")
        s.close()
    except (socket.timeout, ConnectionRefusedError):
        pass
print("-"*35)
