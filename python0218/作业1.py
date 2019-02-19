def up(curentclass,parentclass,attrdict):
    print(curentclass.lower())
    dictclss={}

    for k,v in attrdict.items():
        if not k.startswith("__"):
            dictclss[curentclass.lower()+k.lower()]=v
        if k.startswith("temp"):
            dictclss.pop(curentclass.lower()+k.lower())
    print(dictclss)
class NPC(metaclass=up):
    SPEED=10
    NAME="WZK"
    temp="name"




