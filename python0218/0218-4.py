from  multiprocessing import  Process
import os , time

def fun(name,age,**kwargs):
    print(name,age,kwargs)
    time.sleep(1)
    print(name,age,kwargs)
    time.sleep(2)
    print(name,age,kwargs)
print("parent pid %d"% os.getpid())
p=Process(target=fun, name="child", args=("wzk",20), kwargs={"isalive":False})
p.start()
print("p name %s pid %s"%(p.name,int(p.pid)))
time.sleep(2)
p.terminate()
p.join()
print("child finish")

# def run():
#     print("hello")
#
# class p1(Process):
#     def __init__(self):
#         super().__init__()
#     def run(self):
#         print("进程启用了",os.getpid())
#
# if __name__ == '__main__':
#     P=p1()
#     P.start()
#     print(P.name)
#     run()

