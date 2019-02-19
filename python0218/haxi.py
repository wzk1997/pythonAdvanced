import hashlib
def hash(str1):
    m=hashlib.md5(str1.encode("utf8"))
    print("获取加密的密文，16进制，无参数 ",m.hexdigest)
    print("获取加密的密文，二进制，无参数",m.digest())
    print('获取Hasi的大小',m.block_size)

a=hash('')
print(a)




