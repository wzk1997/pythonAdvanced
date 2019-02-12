class Shop():
    """
    这是一个
        不开张的商店
    """
    isopen=False
    def __init__(self,_name,_price):
        self.name=_name
        self.price=_price
    #类方法
    @classmethod
    def desc(cls):
        # 返回字符串为类说明
        return cls.__doc__
    #静态方法
    @staticmethod
    def stat():
        return ("这是一个静态方法")


shoplist=Shop("钢笔","10元")
print(shoplist.name,shoplist.price)

print(Shop.desc())
print(Shop.stat())
S1=Shop
Shop.ShopingName="不开张的商店"
print(Shop.ShopingName)
print(S1.ShopingName)

S2=Shop("铅笔","五毛")
S2.weight=50
print(S2.weight)

print(Shop.weight)
#类可以调用类属行，但不可以调用实例属性
#实例既可以调用类属行，也可以调用实例属性




