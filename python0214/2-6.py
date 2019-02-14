"""
类装饰器
"""
class Person():
    def __init__(self,fun):
        print("构造函数")
        self.A=fun
    def __call__(self, *args, **kwargs):
        print("类函数")
        self.A()
@Person
def aaa():
    print("你好")
aaa()


"""
装饰器同找方法以及call方法来实现
当程序检测到函数有类装饰器没有直接执行函数
"""