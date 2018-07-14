
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input('请输入数据: ')
    client.sendto(data.encode('utf-8'), ('192.168.2.38', 8081))