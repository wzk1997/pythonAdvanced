"""
给类或者实例动态添加方法
方法：
1实例方法
"""
import types
class Person(object):
    """
    动态添加了一个类方法
    """

    def __init__(self):
        self.name = "wzk"

    def __init__(self,_name):
        self.name=_name



def move(self):
    self.name="wzk"
    return "你好世界"
#动态添加实例方法
a1=Person
a1.move=types.MethodType(move,a1)
print(a1.move())
print(a1.name)



#动态添加类方法
@classmethod
def CLASS(cls):
    return cls.__doc__

Person.CLASS=CLASS
print(Person.CLASS())

#动态添加静态方法
@staticmethod
def HE():
    print("hello")
    return "敲死代码"
Person.HE=HE
print(Person.HE())