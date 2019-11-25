age = int(input("请输入年龄："))
sex = input("请输入性别：")
if age>=18 and sex =="男":
    print("醒醒，搬砖了！")
elif age<18 or sex =="女":
    print("做好饭了没？")
elif sex !='女' and sex !='男':
    print("输入性别有误！")
elif age < 0 or age > 100:
    print("输入年龄有误！")

