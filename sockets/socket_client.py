import socket
import sys

HOST = "localhost"
PORT = 22222


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"Connecting to {HOST}:{PORT}")
    s.connect((HOST, PORT))
    s.send('Hello!'.encode())
    data = s.recv(1024)
    print(data.decode())
