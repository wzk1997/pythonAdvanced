import os


def fourk():
    fun=os.fork()
    print(fun)
    print(fun," 返回当前的进程进程",os.getpid(),"父进程返回子进程",os.getppid())

fourk()