import socket
from datetime import datetime

# Create a TCP server socket
HOST = "localhost"
PORT = 40404

http_response = (
    f"HTTP/1.0 200 OK\r\n"
    f"Server: otusdemo\r\n"
    f"Date: Sat, 01 Jan 2023 10:00:00 GMT\r\n"
    f"Content-Type: text/html; charset=UTF-8\r\n"
    f"\r\n"
)

end_of_stream = '\r\n\r\n'


def handle_client(connection):
    client_data = ''
    with connection:
        while True:
            data = connection.recv(1024)
            print("Received:", data)
            if not data:
                break
            client_data += data.decode()
            if end_of_stream in client_data:
                break
        # Send current server time to the client
        server_utc_time_now = str(datetime.utcnow())
        connection.send(http_response.encode()
                        + server_utc_time_now.encode()
                        + f"\r\n".encode())


def run_server():
    with socket.socket() as serverSocket:
        # Bind the tcp socket to an IP and port
        serverSocket.bind((HOST, PORT))
        # Keep listening
        print(f"Running server on {HOST}:{PORT}...")
        serverSocket.listen()

        while True:
            (clientConnection, clientAddress) = serverSocket.accept()
            handle_client(clientConnection)
            print(f"Sent data to {clientAddress}")


if __name__ == "__main__":
    run_server()
