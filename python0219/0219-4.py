"""
线程 多个线程之间执行没有古顶的先后顺序
"""

from  threading import Thread
import time
def threading(q):
    while True:
        time.sleep(1)
        print(q,"执行了")

def main():
    thread1=Thread(target=threading,args=(1,))
    thread2 = Thread(target=threading, args=(2,))
    thread1.start()
    thread2.start()

if __name__ == '__main__':
    main()

