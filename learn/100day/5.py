"""
水仙花数

for num in range(100,1000):
    low = num % 10
    mid =(num // 10)%10
    high = num // 100
    if low**3 +mid**3 + high**3 == num:
        print("%d 是水仙花数" %num)


for x in range(20):
    for y in range (33):
        for z in range (300):
            if x*5 + y*3 + z/3 == 100 and x + y + z == 100:
                print("公鸡%d只，母鸡%d只，小鸡%d只" %(x,y,z))

CRAPS赌博游戏

from random import randint

money = 1000
while money > 0:
    print("你的总资产为%d"  %money)
    debt = int(input("请输入赌注"))
    need_go = False
    first = randint(1,6)+randint(1,6)
    print("你第一次投出的点数%d" %first)
    if  first == 7 or first == 11:
        money += debt
        print("玩家获胜,剩余资金%d" %money)
        continue
    elif first == 2 or first == 3 or first == 12:
        money -= debt
        print("玩家失败,剩余资金%d" %money)
        continue
    else:
        while True:
            num = randint(1,6)+randint(1,6)
            print("你投出的点数%d" %num)
            print 
            if num == first:
                money += debt
                print("玩家获胜,剩余资金%d" %money)
                break
            elif num == 7:
                money -= debt
                print("玩家失败,剩余资金%d" %money)
                break

斐波那契数列

y = 0
x = 1
for i in range (20):
    x += y
    print(x)
    y += x
    print(y)


完美数

for x in range (1, 10000):
    z = 0
    for y in range (1, x):
        if x % y == 0:
            z += y
    if z == x:
        print("%d是完美数" %x)

"""

for x in range(2, 100):
    check = True
    for y in range(2, x):
        if x % y == 0:
            check = False
    if check == True:
        print(x)

    


    



    


