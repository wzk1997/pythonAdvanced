from multiprocessing import Pool,Manager
import time

def read(num):
    while True:
        time.sleep(1)
        r=num.get()
        print("读出",r,"剩余",num.qsize())
def wread(num):
    l2=[]
    while True:
        time.sleep(0.5)
        for r in range(100000):
            l2.append(r)
        num.put(1)


if __name__ == '__main__':
    num=Manager().Queue(5000)
    pool=Pool(2)
    pool.apply_async(func=read,args=(num,))
    pool.apply_async(func=wread,args=(num,))
    pool.close()
    pool.join()
