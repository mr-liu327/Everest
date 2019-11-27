#定义字符串
name1 =[]
name2 = [1,2,3,'a','b','c',('a',2),{'d':'e'}]
print(name1)
print(name2)

#字符串追加插入和合并
name3 = ['a',1]
print(name3)
name3.append(2)#尾部追加元素,不要将其结果再赋值给另一个变量
print(name3)#a12
name4 = ['b','1']
print(name4)
name41 = ['a','0']
print(name41)
name41.extend(name4)#尾部追加列表 等同于+=,不要再重新赋值
print(name41)
test41 = name4+name41#这个可以重新赋值
print(test41)
name5 = [1,2,3]
print(name5)
name5.insert(0,'0')#给指定位置前插入元素，不要重新赋值
print(name5)
name5[0] = '000'#替换式修改指定位置的元素，不要重新赋值
print(name5)


name6 = [1,2,3,4,5,6]
print(100 in name6)  #判断元素存在与否
print(100 not in name6)


name7 = [1,2,3,4,5,5,5]
print(name7)
print(name7.index(3))#返回指定元素的下标索引
print(name7.count(5))#统计指定元素的个数


name8 = [1,2,3,4,5,6,7,8]
print(name8)
del name8[1]#删除指定位置的元素
print(name8)
test81 = name8.pop()#取出尾部元素
print(test81)
print(name8)
name8.remove(4)#删除指定内容,不要重新赋值
print(name8)


name9 = [1,2,3,4,5,6,7,8,9]
print(name9)
name9.reverse()#逆序,不要重新赋值
print(name9)
test91 = name9[-1::-1]#切片实现逆序,可重新赋值
print(test91)

name10 = [1,3,5,2,4]
print(name10)
name10.sort()#排序，默认从小到大，必须同类元素,不要重新赋值
print(name10)
name10.sort(reverse = True)#修改默认，从大到小，不要重新赋值
print(name10)
name11 = ['a','c','e','b','d']
print(name11)
name11.sort()#不要重新赋值
print(name11)
