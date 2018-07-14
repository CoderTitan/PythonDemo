
import socket


# UDP网络: SOCK_DGRAM
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(('192.168.2.38', 8081))

while True:
    data, add = udp.recvfrom(1024)
    print('受到客户端: ', data.decode('utf-8'))

