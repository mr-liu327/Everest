#while循环
'''
i=0
while i<10:
    i+=1
    if i%2==0:
        print("%d是偶数"%i)
        continue
        print("当前的i是%d"%i)   
        print("OK")
    else:
        print("%d不满足"%i)
print("结束")
'''

#while实现反转字符串
name = 'abcdefg'
l = len(name)
while l>0:
    l-=1
    print(name[l])


#for循环
'''
for i in 'abcdefg':
    print(i)
else:
    print("没有内容")
'''
