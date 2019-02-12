"""
类方法   方法需要使用@classmethod 方法声明 第一个参数class



实例方法  方法的第一个参数 self ， 用来操作实例属性


静态方法   需要使用 @staticmetod 声明
            通过实例，类方法都可以访问
"""


class Person(object):
    """
    这是一个声明类方法的
        用@classmethod来声明
    """
    def __init__(self,name):
        self.name=name
    "用来操作实例的属性"
    def setname(self,newname):
        self.name=newname
    "用来声明类方法"
    @classmethod
    def desc(cls):
        print(cls.__doc__)
    "用来声明静态方法的类"
    @staticmethod
    def stict():
        print("这是一个声明静态方法的类")





p1=Person("wzk")
p1.setname("wk")
print(p1.name)
# Person.stict()
p1.stict()
Person.desc()
