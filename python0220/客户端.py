'''客户端'''
import socket
from threading import  Thread
#接受消息
def ThreadA():
    try:
        while True:
            accpet=clied.recv(1024*1204)
            if len(accpet)==0:
                clied.close()
                break
            else:
                RXD=accpet.decode('gbk')
                print("收到消息",RXD)
    except Exception as  e:
        print(e)
#创建 发线程
def wraead():
    try:
        while True:
            if clied._closed:
                clied.close()
                break
            else:
                #选择用户发送消息
                elect=input('请选择要发送的用户')
                news=input("请输入发送的消息")
                link=elect+"|"+news
                TXD=link.encode('utf-8')
                clied.send(TXD)

    except Exception as e :
        print(e)
if __name__ == '__main__':
    try:
        #创建连接
        clied=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        #创捷接收IP
        IP=('192.168.15.2',9999)
        clied.connect(IP)

        #在一开始的时候输入用户名
        username=input('请输入用户名')
        #转换为utf8形式
        name=username.encode('utf8')
        #将用户名发送过去
        clied.send(name)
        #创建两个线程 一个收  一个发
        read=Thread(target=Thread)
        read.start()
        wraead=Thread(target=wraead)
        wraead.start()
    except Exception as e :
        print(e)


