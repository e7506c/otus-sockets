import socket

# help(socket)

# print(socket.gethostbyname('mail.ru'))
# print(socket.gethostbyname('localhost'))


"""
family:
AF_INET для сетевого протокола IPv4
AF_INET6 для IPv6
AF_UNIX для локальных сокетов (используя файл)
См. https://docs.python.org/3/library/socket.html#socket.AF_INET

type:
SOCK_STREAM (надёжная потокоориентированная служба (сервис) или потоковый сокет) TCP
SOCK_DGRAM (служба датаграмм или датаграммный сокет) UDP
См. https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM

"""

my_socket = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_STREAM,
)

print(my_socket)

my_socket.close()
