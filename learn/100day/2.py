"""
f = float(input("请输入华氏摄氏度"))
c = (f-32)/1.8
print('%.1f华氏度 = %.1f摄氏度' %(f,c))


radius = float(input("请输入半径"))
perimeter = 2* radius*3.1416
area = 3.1416*radius**2
print('周长为%.2f,面积为%.2f' %(perimeter,area))
"""
year = int(input("请输入年份"))
is_Leap = year % 4 == 0 and year % 4 != 0 \
    or year % 400 == 0
print(is_Leap)