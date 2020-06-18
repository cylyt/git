"""
sum = 0
for x in range(0,101,2):
    sum+=x
print(sum)


import random
answer = random.randint(1,100)
counter = 0
while True:
    counter += 1
    number = int(input("请输入数字"))
    if number > answer:
        print("小一点")
    elif number < answer:
        print("大一点")
    else:
        print("猜对了！")
        break
print("一共猜了%d次" %counter)


for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d" %(i,j,i*j), end="\t")
    print()



number = int(input("输入一个正整数"))
x=True
for i in range(2, number):
    if number % i == 0:  
        x=False
        break
if x == True:
    print("%d 是素数" %number)
elif x == False:
    print("%d 不是素数" %number)


a = int(input("请输入第一个数"))
b = int(input("请输入第二个数"))
if a > b:
    a, b = b, a
for i in range(x,1,-1):
    if a % i == 0  and b % i == 0:
        print("%d和%d的最大公约数是",% (a, b, i))
        print("%d和%d的最小公倍数是",% (a, b, a*b//i))
        break
"""
line = int(input("请输入行数"))
for i in range (line):
    for j in range (i+1):
        print("*", end="")
    print()
for i in range(line):
    for x in range(line-i-1):
        print(" ",end="")
    for y in range(i+1):
        print("*",end="")
    print()
for i in range (line):
    for y in range(line-i-1):
        print(" ", end="")
    for x in range(2*i+1):
        print("*",end="")
    print()