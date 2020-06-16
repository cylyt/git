"""
value = float(input("请输入长度："))
unit = input("请输入单位: （英寸/厘米/in/cm）")
if unit == "英寸" or unit == "in":
    print('%.2f 英寸 = %.2f厘米' %(value,value * 2.54))
elif unit == "厘米" or unit == "cm":
    print('%.2f厘米 = %.2f英寸' %(value,value / 2.54))
else:
    print("输入不合法")

score = float(input("请输入成绩"))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("E")
"""
a = float(input("a边长"))
b = float(input("b边长"))
c = float(input("c边长"))