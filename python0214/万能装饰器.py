
def Person(fun):
    def Per(*args,**kwargs):
        user=input("请输入用户名")
        pasd=int(input("请输入密码"))
        if user=="admin" and pasd==123456:
            return fun(*args,**kwargs)
        else:
            print("登陆失败")
    return Per
@Person
def shoplist(a,b,c,d,e,f):
    print("第一个数字%s,第二个数字%s,第一个数字%s,第二个数字%s,"%(a,b,c,d,))
shoplist(1,2,2,4,5,35)
@Person
def HE():
    print("hello")
HE()