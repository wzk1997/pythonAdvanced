import socket
#创建服务器
sever=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定ip地址和端口号
sever.bind(('192.168.15.2',8888))

#阻塞消息
while True:
    recvdata, recvaddr = sever.recvfrom(1024)
    print("接收到了消息",recvaddr,recvdata.decode('utf8'))
    sever.sendto(recvdata,recvaddr,)

