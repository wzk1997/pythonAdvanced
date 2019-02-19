"""
加锁解锁
"""

from threading import Lock,Thread
lock=Lock()
num=0
def therea():
    global num
    for i in range(10000):
        lock.acquire()
        num=num+1
        lock.release()
if __name__ == '__main__':
    there1=Thread(target=therea)
    there2=Thread(target=therea)
    there1.start()
    there1.join()
    there2.start()
    there2.join()
    print(num)

