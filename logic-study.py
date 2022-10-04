"""result = 10 > 8
print(f"10 > 8 的结果是: {result},类型是:{type(result)}")
print("10 > 8 的结果是: {result},类型是:{type(result)}")
print(f"10 > 8 的结果是: result,类型是:{type(result)}")

result = "it" == "itt"
print(f"字符串it和itt是否相等，结果是{result},类型是:{type(result)}")

age1 = 10
print(f"我今年{age1}岁")

if age1 >= 18:
    print("成年","读大学")

print("11")

age2 = 19
print(f"我今年{age2}岁")

if age2 >= 18: #不要忘记引号
    print("成年","读大学")

print("22")

print("欢迎来到儿童游乐场，儿童免费，成人收费10元")
age = int(input("输入年龄："))
if age >= 18:
    print("成年，收费10元hh")

else:
    print("未成年，免费")

print("祝您愉快")

print("欢迎来到动物园")
height1 = int(input("输入身高:"))
if height1 >= 120:
    print("收费10元")
else:
    print("免费mf")

print("欢迎来到动物园")
height2 = int(input("输入身高:"))
vip_level = int(input("输入vip等级(1-5):"))
if height2 < 120 :
    print("免费")
elif vip_level > 3:
    print("免费ll)
else:
    print("10yuan")

print("欢迎来到动物园")
if int(input("输入身高:")) < 120 :
    print("免费")
elif int(input("输入vip等级(1-5):")) > 3:
    print("免费")
else:
    print("10yuan")

print("欢迎来猜数字")
if int(input("输入猜想的数字:")) == 10 :
    print("猜对啦")
elif int(input("不对，第二次机会:")) == 10 :
    print("猜对啦")
elif int(input("第三次机会:")) == 10 :
    print("猜对啦")
else:
    print("错了")"""


if int(input("输入身高:")) > 120 :
    print("收钱")
    if int(input("输入vip等级(1-5):")) > 3:
        print("mf")
    else:
        print("10")
else:
    print("mf")


