'''
动态语言(解释性语言)：执行需要解释器，根据需要去解释语言，效率低下

编译性语言：需要预先编译成机器语言或者中间语言，效率搞

很多python库使用C语言来编写 如import math
胶水语言（自己不是先，通过调用其他语言来实现）


python 如何动态
'''
class  Person(object):
    "只能在表明里边添加name mp hp 这些属性的时候才能正常添加 其他添加后报错"
    __slots__ = ("name","mp","hp")
    '类属性'
    Alice=False
    def __init__(self,_hp):
        self.hp=_hp

P1=Person(50)
P1.hp=100
print(P1.hp)
"声明的时候还没有name属性 现在动态添加物一个"
P1.name="wzk"
print(Person.name)
"动态添加"
P1.mp=411
print(Person.mp)

