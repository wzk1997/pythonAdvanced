# #1，编写代码验证
# 类可以操作类属性，不可以操作实例属性
# 实例可以操作实例属性，可以操作类属性
class Person():
    "类属行"
    name="wzk"
    def __init__(self,_hp):
        "实例属性"
        self.hp=_hp
#类可以操作类属行 不可以操作实例属性
print(Person.name)
print(Person.hp)
#实例可以操作类属行 也可以操作实例属性
s1=Person(100)
print(s1.hp)
print(s1.name)
