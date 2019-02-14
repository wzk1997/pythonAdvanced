import time
def check(fun):
    def timeS():
        a=time.time()
        fun()
        b = time.time()
        print("当前的%s秒"%(b-a))
    return timeS

@check
def che():
    sum=0
    for i in range(100):
        for j in range(100):
            sum+=i*j
            print(sum)
che()


import time,random
def outer(fun):
    def timeS():
        start_time = time.time()
        fun()
        int_time=time.time()
        print("运行时间为%s"%(int_time-start_time))
    return timeS
def index():
    a=time.sleep(random.randrange(1,10))
    print(a)
    print("欢迎")
index=outer(index)
index()