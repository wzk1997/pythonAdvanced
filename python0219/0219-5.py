from threading import Thread
# num=0
# def threadA():
#     for i in range(1000000):
#         global num
#         num=num+1
# def threadB():
#     for i in range(1000000):
#         global num
#         num=num+1
# if __name__ == '__main__':
#     thread1=Thread(target=threadA)
#     thread2=Thread(target=threadB)
#     thread1.start()
#     thread1.join()
#     thread2.start()
#     thread2.join()
#
#     print(num)





num=0
def fun1():
    global num
    for i in range(100000):
        num=num+1
fun=Thread(target=fun1)
fun.start()

print(num)

class thread(Thread):
    def run(self):
        global num
        for   i  in range(100000):
            num=num+1
        print(num)
t1=Thread(target=thread)

t1.start()
fun.join()
t1.join()
