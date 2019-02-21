import socket
from threading import  Thread

#收入客户端的消息
def cll(cli):
        data=cli.recv(1024*1024)
        print('收到消息',data.decode('gbk'))
#收入进程
def take():
    while True:
        cliked,clikedaddr=server.accept()
        print("客户端连接",clikedaddr)
        There=Thread(target=cll,args=(cliked,))
        There.start()

#主函数
if __name__ == '__main__':
    #创建一个接受列表
    cliekList=[]
    #创建连接
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定服务器IP
    server.bind(("192.168.15.2",9999))
    #开始监听
    server.listen()
    #创建一个两个线程 一个接受 一个发送
    serverTread=Thread(target=take)
    serverTread.start()

