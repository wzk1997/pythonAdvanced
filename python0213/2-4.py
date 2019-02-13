"""
生成器 迭代器

"""
#Iterable  判断是否可以迭代  可以for 循环的都是可迭代对象
#如 list列表类型 tuple元祖类型 dict 字典类型 set集合 类型 str字符串类型 生成器类型也可以for循环
#不可以for 循环的不是迭代类型
#int 整型 float

from collections.abc import Iterable
from collections.abc import Iterator
g=[x for x in range(10)]
g2=(x for x in range(10))
print(isinstance([],Iterable))
print(isinstance((),Iterable))
print(isinstance({},Iterable))
print(isinstance(([]),Iterable))
print(isinstance("",Iterable))
print(isinstance(1.2,Iterable))
print(isinstance(100,Iterable))
print(isinstance((x for x in range(10)),Iterable))
print("Iterator  判断是否是迭代器")
print(isinstance([],Iterator))
print(isinstance((),Iterator))
print(isinstance({},Iterator))
print(isinstance(([]),Iterator))
print(isinstance("",Iterator))
print(isinstance(1.2,Iterator))
print(isinstance(100,Iterator))
print(isinstance((x for x in range(10)),Iterator))