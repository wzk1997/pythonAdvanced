import os

pip=os.fork()

if pip==0:
    print("获取子子进程%s，获取父进程%s"%(pip,os.getppid()))
else:
    print("获取父进程ID%s"%os.getpid())