#声明完之后，长度固定，只可查，不可改(增删改)，但你列表元素的内嵌元素可修改
#有序，rang(1,10)  开始必须是小的
#访问元素同列表，通过下标访问，count和index方式同列表


#声明元组tuple
names = ['a','b','c']
my_tuple = ('abc',100,names)
print(my_tuple)

my_tuple[-1][0] = 1 #可以通过下标修改元组内部的可修改元素
print(my_tuple)

#range(1,10),  py2得到列表，py3得不到，需通过循环得到。
