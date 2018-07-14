

import socket
# 网络编程所需的库

# 1. 创建一个socket
# 参数一: 指定协议, AF_INET(Ipv4)  或 AF_INET6(Ipv6)
# 参数二: 使用面向流的TCP协议
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 2. 建立连接
# 参数: 是一个元组, 第一个元素为要连接的IP地址, 第二个参数为端口
sk.connect(("www.sina.com.cn", 80))

# b: 字节码
sk.send(b"GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n")

# 等待接受数据
data = []
while True:
    # 每次接受1K的数据
    tempData = sk.recv(1024)
    if tempData:
        data.append(tempData)
    else:
        break


dataStr = (b"".join(data)).decode("utf-8")

# 断开连接
sk.close()

# print(dataStr)


header, HTML = dataStr.split('\r\n\r\n', 1)
print(header)
print('-----------')
print(HTML)