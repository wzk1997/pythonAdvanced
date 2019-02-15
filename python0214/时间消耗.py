import time
def cost(f):
    def fun():
        start_time=time.time()
        f()
        end_time=time.time()
        print("时间消耗为%s"%(end_time-start_time))
    return fun


#
# @cost
# def tuype():
#     x=(x for x in range(100000000000000000000000000000000000000000000000000000000000000000000000000))
#     for i in x:
#         print(i)
# tuype()

@cost
def lista():
    x=[g for g in range(10000)]
    print(x)
lista()