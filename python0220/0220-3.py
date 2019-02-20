'''
创建客户端
'''

import socket
# #创建客户端
# clect=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #发送数据到指定对象
# clect.sendto("你好服务器".encode('utf8'),('192.168.15.2',9999))
# #客户端调用阻塞数据方法
# recvdata,recvaddr=clect.recvfrom(1024)
# print("你好服务器",recvaddr.decode('utf8'),"你好",recvdata)


#创建udp客户端
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#发送数据到指定对象

client.sendto("你好".encode('utf8'),('192.168.15.2',888))
#客户端调用阻塞方法接受shuju
BUFFRSIZE=1024
revedata,revaddr=client.recvfrom(BUFFRSIZE)
print("收到了",revaddr,"消息",revedata.decode('utf8'))