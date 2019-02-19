from  multiprocessing import process,Pool
import os
import time

def Pro(**kwargs):
    time.sleep(1)
    print("当前进程",os.getpid(),"循环次数为",kwargs)

if __name__ == '__main__':
    pool=Pool(2)
    for i in range(5):
        pool.apply_async(Pro,kwds={"次数":i})
    pool.close()
    pool.join()
