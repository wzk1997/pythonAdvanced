'''
tcp服务端
'''
import socket
#创建服务端
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定ip

server.bind(("192.168.15.2",7777))
#开始监听
server.listen()
#获取客户端
cliic,cliicaddr=server.accept()
print("客户端",cliicaddr,)
#接受客户端数据
cliic.recv(1024)
print("收到了数据",cliic.recv(1024).decode('utf-8'))

