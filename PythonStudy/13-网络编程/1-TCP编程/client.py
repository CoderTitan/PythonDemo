
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.2.38', 8081))

while True:
    data = input('输入要给服务器发送的数据')
    client.send(data.encode('utf-8'))
    info = client.recv(1024)
    print("服务器说: ", info.decode('utf-8'))