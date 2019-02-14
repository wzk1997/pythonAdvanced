# def cheakuser(fun):
#     def user():
#         username=input("请输入用户名")
#         if username=="wzk":
#             fun()
#         else:
#             print("未经授权")
#     return user
# @cheakuser
# def order():
#     for i in range(10):
#         print("查看订单",i)
# order()
# @cheakuser
# def money():
#     print("账户余额为1000大洋")
# money()

# from  urllib.request import urlopen
#
# def index(url):
#     def get():
#         return urlopen(url).read()
#     return get
#
# python=index("http://www.python.org")
# print(python())
# baidu=index("http://www.baidu.com")
# print(baidu())

import time,random
def outer(fun):
    def timeS():
        start_time = time.time()
        fun()
        int_time=time.time()
        print("运行时间为%s"%(int_time-start_time))
    return timeS
def index():
    time.sleep(random.randrange(1,5))
    print("欢迎")
index=outer(index)
index()