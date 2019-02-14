def Person(fun):
    def Per():
        username=input("请输入用户名")
        if username=="wzk":
            fun()
        else:
            print("验证失败")
    return Per

@Person
def listA():
    for i in range(10):
        print("订单列表",i)
listA()
@Person
def money():
    mone=100
    print("用户余额为%s"%mone)
money()