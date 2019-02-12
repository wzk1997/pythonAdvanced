print("你好呀")
class Person():
    name="wzk"
    def __init__(self,_age):
        self.age=_age

s1=Person(1)
s2=Person(2)
Person.name="wk"
print(s2.name,s2.age)
print(s1.name,s1.age)

