def fun(c):
    a,b=0,1
    yield a
    yield b
    conte=0
    while conte<c:
        a,b=b,a+b
        yield b
        conte+=1
a=fun(10)
while True:
    try:
        f=next(a)
        print(f)
    except StopIteration as e:
        print(e)
        break
# 简单方法
def fan():
    yield 10
    yield 20
    yield 30
    return "hello"
Ri=fan()
print(next(Ri))
print(next(Ri))
print(next(Ri))

try:
    print(next(Ri))
except StopIteration as e:
    print(e)
