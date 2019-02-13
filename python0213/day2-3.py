"""
生成器的第二种写法
必须在函数内部使用
 通过函数+yield
  函数的内部有yield 函数返回为生成器

"""

def fun():
    yield 10
    yield 20
    yield 30
    return "hello word"

# a=fun()
# print(next(a))
# print(next(a))
# print(next(a))
# try:
#     print(next(a))
# except StopIteration as e:
#     print(e)
def fan(num):
    a,b="*","*"
    yield a
    yield b
    count=0
    while count<=num:
       a,b=b,a+b
       yield b
       count+=1

a=fan(2)
while True:
    try:
        b=next(a)
        print(b)
        if fan==50:
            break
    except StopIteration as e:
        print(e)
        break
