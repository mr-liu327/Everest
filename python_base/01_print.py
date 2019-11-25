# -*- coding:UTF-8 -*-
name = raw_input("请输入姓名：")
age = input("请输入年龄：")
age = int(age)+2
print("输入姓名：%s,年龄为：%s"%(name,age))
#py2识别age+2为表达式，正常输出，无需转换
#py3识别age+2为字符串，输出有误，需要使用int(age)强制转换为整型
#raw_input是py2的输入方法
#input是py3的输入方法
#py2的print是一种输出语句
#py3的print的输出是一个函数

#格式化输出整数
#b = "the length of (%s) is %d" %('Hello python2',len('Hello Python2'))
