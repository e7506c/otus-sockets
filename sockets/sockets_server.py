import socket
from random import randint

HOST = 'localhost'
# PORT = randint(20000, 30000)
PORT = 22222

my_socket = socket.socket()

host_port = (HOST, PORT)

my_socket.bind(host_port)
print("Started socket on ", host_port)

my_socket.listen(1)

conn, addr = my_socket.accept()
print("Got connection from ", conn, addr)

# Receive data from socket
data = conn.recv(1024)
print("Got data\n", data.decode("utf-8"))

# Send data to the client
response = 'HTTP/1.1 200 OK\nContent-Type: text/html\n\n<html><body><h1>Hello World!</h1></body></html>'
conn.send(response.encode())

my_socket.close()
