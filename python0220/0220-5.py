'客户端'

import socket
#创建客户端
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('192.168.15.2',7777))
#给客户端发送数据
client.send("你好服务端".encode('utf-8'),)
