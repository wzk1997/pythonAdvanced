"""
函数内部嵌套函数
内部函数可以访问外部函数
外部函数将内部函数返回
"""
def fun1(a):
    def fun2(b):
        return a+b
    return fun2
print(fun1(5),type(fun1))

a=fun1(5)(6)
print(a)

# a=fun1()
# print(a(5))
