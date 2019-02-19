from threading import Thread
import  time,threading

# start=time.time()
# for i in range(5):
#     prt()
# end=time.time()
# print("循环时间为",(end-start))

#
# def prt():
#     print("hello")
#     time.sleep(1)
# start=time.time()
# def halou():
#     for i in range(5):
#         t=threading.Thread(target=prt)
#         t.start()
#     end=time.time()
#     print("循环时间为",(end-start))
#

def fun(q):
    for i in range(0,int(q)):
        print("hello",threading.Thread ,"次数为",q)
def main(q):
    listA=list()
    for i in range(0,q):
        num=("thead%s"%i)
        listA.append(threading.Thread(target=fun,name=num,args=(20,)))
    for j in listA:
        j.start()
        j.join()
if __name__ == '__main__':
    main(3)

