#创建客户端
import socket
clect=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#发送数据到指定对象

#客户端调用阻塞数据方法
while True:
    name = input("请输入消息")
    clect.sendto(name.encode('utf8'), ('192.168.15.2', 8888))
    recvdata,recvaddr=clect.recvfrom(1024)
    print("收到",recvaddr,recvdata.decode('utf8'),)



