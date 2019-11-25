name = 'abcdefg'
print('字符串长为：%d'%(len(name)))


name2 = 'abcd'
print('索引字符串第二个字符是：%s'%name[1])


name3 = 'abcdefghijklmn'
print('切片结果为：'+name[0:6:1])


name4 = 'hhhjklmnopqrstuvwxyz'
print('从左开始数a的下标位置为：%d'%name4.find('a'))
print('从左开始数o的下标位置为：%d'%name4.rfind('o'))
print('获取l元素在这个字符串内的索引值:%d'%name4.index('l'))


name5 = 'aaabbc'
print('统计a出现的次数：%d'%name5.count('a'))


name6 = 'aaabbbccc'
print('用d替换掉两个字符串中的b：%s'%name6.replace('b','d',2))

name7 = 'this is a test'
print('以空格隔开字符串元素,返回列表：%s'%name7.split(' '))

name8 = 'wo zhen de yao lie le '
print('只分隔两段：%s'%name8.split(' ',2))
#大概返回的是列表，分隔只能用空格吧，我换其他的居然不能达到预期。
#splitlines()是按换行符分隔，等同于split('\n')


name9 = 'this is a simle test!'
test9 = name9.partition("a")
print(test9)
#返回的是元组类型，以a分隔整个字符串。


name10 = 'this is a test too'
test10 = name10.capitalize()
test101 = name10.title()
print(test10)
print(test101)
#返回的还是一个字符串，但是首单词字母大写了。

name11 = 'first test'
test11 = name11.upper()
test111 = name11.lower()
print(test11)
print(test111)
#全部转换成大写或小写


file_name = 'lz.txt'
if file_name.endswith(".txt"):
    print('这是一个文本。')
#判断末尾是否是指定结尾


name12 = 'second test'
print(name12.ljust(15,'*'))
#左对齐，右补充，字符串补足15位。还有rjust center


name13 = '   third   test'
print(name13.lstrip())
#去除字符串左空白，同理还有右rstrip，左右strip


a = '123'
b = 'abc'
c = '123abc'
testa=a.isalpha()#0  全数字
testb=b.isalpha()#1
testc=c.isalpha()#0
testd=c.isdigit()#0  全字母
teste=c.isalnum()#1  全字母或数字
testf=c.isspace()#0  全空格
print(testa)
print(testb)
print(testc)
print(testd)
print(teste)
print(testf)







