"""
装饰器的形成
"""

def cheakuser(fun):
    def user():
        username=input("请输入用户名")
        if username=="wzk":
            fun()
        else:
            print("未经授权")
    return user



def abc():
    print("授权成功")
abc=cheakuser(abc)
abc()