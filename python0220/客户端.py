'''客户端'''
import socket
from threading import  Thread

def ThreadA():
        while True:
            sendstr = input("请输入发送内容")
            if sendstr == "exit":
                clied.close()
                break
            else:
                sendbytes = sendstr.encode("utf-8")
                clied.send(sendbytes)
def ThreadB():
    while True:
        if not  clied._closed:
            databytes = clied.recv(1024)
            datastr = databytes.decode("utf-8")
            print("收到", datastr)
        else:
            break




if __name__ == '__main__':
    #创建衔接
    try:
        clied=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #绑定ip
        clied.connect(('192.168.15.2',9999))
       #设置用户名
        name=input("请输入用户名")
        clied.send(name.encode('utf-8'))
        # 开启线程
        t1=Thread(target=ThreadA)
        t1.start()
        t2=Thread(target=ThreadB)
        t2.start()
    except Exception as  e:
        print(e)


