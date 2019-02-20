"""
多线程耗时
"""
import time
from threading import Thread

def fun():
    time.sleep(1)
    print("+")


def threadfor():
    "创建线程"
    listA = []
    start=time.time()
    for i in range(5):
        t1 = Thread(target=fun)
        t1.start()
        listA.append(t1)
    for r in listA:
        r.join()
    end=time.time()
    print("耗时",end-start)
if __name__ == '__main__':
    threadfor()