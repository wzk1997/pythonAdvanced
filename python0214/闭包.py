def Person():
    a=1
    def avc():
       b=a+1
       print(b)
    return avc
a=Person()
a()