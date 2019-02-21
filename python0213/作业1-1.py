# Iterable判断是否可以迭代
from collections.abc import Iterable
#Iterator 判断是否是迭代器
from collections.abc import Iterator
li=[1,2,3,4,5,6,7,8]
tp=(1,2,3,4,5,6,8,1,)
dic={"id":1,"name":"wzk","addr":"xinxiang"}
STR="abcdefg"
INT=100
#判断是否可以迭代
print(isinstance(li,Iterable))
print(isinstance(tp,Iterable))
print(isinstance(dic,Iterable))
print(isinstance(STR,Iterable))
print(isinstance(INT,Iterable))
#判断是否是迭代器
print(isinstance(li,Iterator))
print(isinstance(tp,Iterator))
print(isinstance(dic,Iterator))
print(isinstance(STR,Iterator))
print(isinstance(INT,Iterator))
g=(X for X in range(10))
print(isinstance(g,Iterable))
print(isinstance(g,Iterator))
while True:
    try:
        r=next(g)
        print(r)
    except StopIteration as e:
        print(e)
        break

