from  multiprocessing import Manager,Pool
import time

def read(q):
    while True:
        time.sleep(1)
        print("读出",q.get())

def wread(q):
    for i in range(10):
        q.put(i)
        print("读入",i)
        time.sleep(2)

if __name__ == '__main__':
    q=Manager().Queue(5000000)
    pool=Pool()
    pool.apply_async(read,args=(q,))
    pool.apply_async(wread,args=(q,))
    pool.close()
    pool.join()
