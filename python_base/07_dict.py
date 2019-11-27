#键值对形式，一个键值对即一个元素
#值可以重复，键不可以重复(会覆盖)且不可以是可变类型。
#无序，不可通过下标访问，通过键访问。
#通过键查找，查找速度极快。



#声明字典dict
my_dict = {'name':'lz','gender':'man','age':18}
my_dict.get('address')#访问没有，返回空，不会报错
#my_dict['address']  #返回报错
print(my_dict)

my_dict['dizhi'] = 'beijing'#添加键值
print(my_dict)
my_dict['address'] = 'beijing'
print(my_dict)
my_dict['dizhi'] = 'nanjing'#修改键值
print(my_dict)
del my_dict['dizhi']#删除键值，del回收内存，clear不回收内存
print(my_dict)
print('dizhi' in my_dict)#判断键在字典内没
