'''
udp 服务器端
# '''
# import socket
# #创建服务器
# sever=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #绑定ip地址和端口号
# sever.bind(('192.168.15.2',9999))
# #阻塞消息
# recvdata,recvaddr=sever.recvfrom(1024)
# print("接收到了消息".encode('utf8'),recvaddr,'你好',recvdata.decode('utf8'))
# print("服务端结束")





















#
#创建udp服务器
import socket
sever=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口
SERVERBIND=('192.168.15.2',888)
sever.bind((SERVERBIND))
#开始使用阻塞消息
BUFFRSIZE=1024
revedata,reveaddr=sever.recvfrom(BUFFRSIZE)
print("收到了",reveaddr,"收到了",revedata.decode("utf8"))
sever.sendto("收到了消息".encode("utf8"),reveaddr,)

#

