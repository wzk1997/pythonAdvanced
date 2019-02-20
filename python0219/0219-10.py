import time
from threading import Thread


def fun(name):
    while True:
        time.sleep(1)
        print("执行",name)
def main():
    while True:
        time.sleep(1)
        t1=Thread(target=fun,args=(1,))
        t2=Thread(target=fun,args=(2,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
if __name__ == '__main__':
    main()