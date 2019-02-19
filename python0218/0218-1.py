# # def move(self,move):
# #     print("AI的速度为%s"%move)
# #
# #
# # AI=type()
#
#
#
#
# """
# 要求 所有的书写均要以小写类名+小写属性
#
# metaclass 存储的方法才是真正类的创建过程
#
# python 创建
# """
def renameattribute(classname,parentclass,attributedic):
    newattrobute={}
    for k,v in attributedic.items():
        if not k.startswith("__"):
            key=classname.lower()+k
            newattrobute[key] = v
    for k,v in newattrobute.items():
        print(k,v)
    return type(classname,parentclass,attributedic)

class AI(object,metaclass=renameattribute):
    isalive=False

a=AI()
print(hasattr(a,"isalive"))
print(hasattr(a,"aiisalive"))
