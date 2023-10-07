# portscanner
# dibuat oleh fixploit14

import socket

alamat_ip = input("Masukkan alamat IP: ")
daftar_port = input("Masukkan daftar port yang dipisahkan dengan koma (contoh: 80,443,22): ").split(',')
daftar_port = [int(port) for port in daftar_port]

socket.setdefaulttimeout(5)

for port in daftar_port:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((alamat_ip, port))
        print(f"Port {port} terbuka")
        s.close()
    except (socket.timeout, ConnectionRefusedError):
        pass
