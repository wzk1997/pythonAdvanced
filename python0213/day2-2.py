"""
生成器
"""
"列表模式 很好用 缺点 多少元素开辟多少空间"
#列表模式可以用下标
L1=[a for a in range(3)]
# print(L1,L1.__sizeof__())
print(L1[1])
print('列表使用for 循环')

for b in L1:
    print(b)
"成器写法 跟对象元素个数无关"
"生成器不能用下标 但是可以用next（生成器对象） 和for 循环"
"生成器的后面的数是推算出来的"



L2=(a for a in range(5))
#生成器后面的推算出来的 不能用下标 但是可以用for 循环
print(next(L2),next(L2),next(L2))
print("生成器使用for循环")
for a in L2:
    print(a)