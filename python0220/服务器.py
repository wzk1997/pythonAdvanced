import socket
from threading import  Thread
def tread():
    data=
#TODO 到这没看懂
def Tread1():
    pass
def Tread2():
    while True:
        serverdata,serveraddr=server.accept()

#主函数
if __name__ == '__main__':

#创建衔接
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定IP
    server.bind(('192.168.15.2',9999))
    #开启监听
    server.listen()
    #开启线程
    t1=Thread(target=Tread1)
    t2=Thread(target=Tread2)
    t1.start()
    t2.start()



