'''
进程
'''


from multiprocessing import ProcessError
from multiprocessing import Queue,Process,Pool,Manager
import time
"基础使用"
# q = Queue()
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# q.put(5)
# q.put(6)
# print(q.empty())
# print(q.qsize())
# print(q.full())
"""
使用Queqe 完成多线程共享
"""
q = Queue(10)
q.put(-2)
q.put(-1)
def read(q):
    while True:
        time.sleep(1)
        print("长度",q.qsize())
        print("读入数据",q.get())


def write(q):
    for i in range(10):
        q.put(i)
        time.sleep(2)

if __name__ == '__main__':

    pr=Process(target=read,args=(q,))
    pw=Process(target=write,args=(q,))

    pr.start()
    pw.start()

    pr.join()
    pw.join()




