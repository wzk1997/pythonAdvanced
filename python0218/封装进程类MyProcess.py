from multiprocessing import Process
import os
class MyProcess(Process):
    def __init__(self,group=None, target=None, name=None, args=(), kwargs={}):
        super().__init__(group,target,name,args,kwargs)
    def run(self):
        print("进程启用了")
if __name__ == '__main__':
    p1=MyProcess()
    print(p1.name)
    p1.start()
    p1.join()

