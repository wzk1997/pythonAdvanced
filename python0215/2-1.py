# list1=[1,2,3,4,[5,6,7]]
# #list2=[1,2,3,4,[5,6,7]]
# list1.append([5,[7,8]])
# list2=list1
# print(list1)
# print(id(list1))
# print(id(list2))



import copy
#浅拷贝   列表外层生成独立空间，内层拷贝引用（拷贝内层地址）
# listA=[1,2,3,4,[5,6]]
# listb=listA.copy()
# print(id(listA))
# print(id(listb))
# listA.append([2,2,3])
# listb.append(5)
# print(listA)
# print(listb)

'深拷贝  外层 和内城都创建内存知地址，拷贝引用'
listA=[1,2,3,4,[5,6]]
listB=copy.deepcopy(listA)
listA.append(7)
listB.append([4])
print(listA)
print(listB)
print(id(listA),id(listA[4]),id(listA[5]))
print(id(listB),id(listB[4]))




list1 = [1,2,[3,4]]
print(list1)
list2 = copy.deepcopy(list1)
print(list2)
list1.append(5)
print(list1,list2)
list1[2].append(3.5)
print(list1,list2)