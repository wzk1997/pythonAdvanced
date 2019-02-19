import os,time
from multiprocessing import Process
#print(Process.__dict__)
def ProcessA():
    print("进程A执行了",os.getpid())

def main():
    print("主进程ID",os.getpid())
    p1=Process(name="进程A",target=ProcessA,)
    p1.start()
    p1.join()






if __name__=="__main__":
    main()