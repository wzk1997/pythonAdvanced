# 新建2.py文件编码验证迭代器与可迭代的区别
from collections.abc import Iterator,Iterable

a=(x for x in range(10))
print(next(a),next(a),next(a),next(a))
for i in a:
    print(next(a))
#判断是否可以迭代对象
print(isinstance(a,Iterable))
#判断是否是迭代器
print(isinstance(a,Iterator))
listA=[1,2,3,4,5,6,7,8,9]
#判断是否可以迭代对象
print(isinstance(listA,Iterable))
for i in listA:
    print(i)
#判断是否是迭代器
print(isinstance(listA,Iterator))
print(next(listA))
#迭代器可以使用 for in 循环 并切可以用next回调
#迭代对象可以使用for in 循环但不可以使用next回调