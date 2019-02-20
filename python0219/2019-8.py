from multiprocessing import Pool,Manager,Process,Lock
import time
from threading import  Thread
#
# def read(num):
#     while True:
#         time.sleep(1)
#         r=num.get()
#         print("读出",r,"剩余",num.qsize())
# def wread(num):
#     l2=[]
#     while True:
#         time.sleep(0.5)
#         for r in range(100000):
#             l2.append(r)
#         num.put(1)
#
#
# if __name__ == '__main__':
#     num=Manager().Queue(5000)
#     pool=Pool(2)
#     pool.apply_async(func=read,args=(num,))
#     pool.apply_async(func=wread,args=(num,))
#     pool.close()
#     pool.join()





num=0
lock=Lock()
def fun():
    global num
    lock.acquire()
    for i in range(10000000):
            num=num+1
    lock.release()

if __name__ == '__main__':
    t1=Thread(target=fun)
    t1.start()
    t2 = Thread(target=fun)
    t2.start()
    t2.join()
    t1.join()

    print(num)
