def chenkuser(fun):
    def chenk():
        username=input("请输入用户名")

        if username=="wzk":
            fun()
        else:
            print("授权失败")
    return chenk
@chenkuser
def shoulist():
    print("展示列表成功")
    cont = input("请输入页数")
    if cont==1 and cont==2:
        print("你好")
shoulist()
print(shoulist())
