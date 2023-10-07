import socket

ipaddress = input("Masukkan alamat ip: ")
daftar_port= input("Masukkan nomor port yang dipisahkan dengan koma (misalnya: 80,443,22): ").split(',')
daftar_port= [int(port) for port in ports]

socket.setdefaulttimeout(5)

for port in daftar_port:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        print(f"Port {port} terbuka")
        s.close()
    except (socket.timeout, ConnectionRefusedError):
        pass
