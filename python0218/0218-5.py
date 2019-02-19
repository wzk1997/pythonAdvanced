from multiprocessing import  Process,Pool
import os ,time

def pro(**kwargs):
    time.sleep(2)
    print("当前的进程为", os.getpid(), "循环次数为", kwargs)
if __name__ == '__main__':

    pool = Pool(2)
    for i in range(5):
        pool.apply(pro, kwds={"次数": i})
    pool.close()
    pool.join()  # 阻塞函数
    print("结束")
