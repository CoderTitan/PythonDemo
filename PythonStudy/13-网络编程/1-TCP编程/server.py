
import socket

# 1. 创建socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP端口
server.bind(('192.168.2.38', 8081))


# 监听
server.listen(5)
print('服务器启动成功.')


# 等待链接
clientSocker, clientAddress = server.accept()

print('%s ------- %s 连接成功' % (str(clientSocker), clientAddress))

while True:
    data = clientSocker.recv(1024)
    print('客户端说: ' + data.decode('utf-8'))
    sendData = input('输入需要返回给客户端的信息: ')
    clientSocker.send(sendData.encode('utf-8'))






