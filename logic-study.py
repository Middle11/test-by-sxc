result = 10 > 8
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
    print("成年，收费10元")

else:
    print("未成年，免费")

print("祝您愉快")

print("欢迎来到动物园")
height = int(input("输入身高:"))
if height >= 120:
    print("收费10元")
else:
    print("免费")

