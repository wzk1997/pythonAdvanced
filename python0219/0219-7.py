from multiprocessing import Process,Queue
import time
q=Queue()
q.put(1)
q.put(2)

def main1():
    while True:
        time.sleep(1)
        print("取出数据",q.get())
def main2():

    for i in range(5):
        time.sleep(2)
        print("加入数据",i)
if __name__ == '__main__':
    p1=Process(target=main1)
    p2=Process(target=main2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
