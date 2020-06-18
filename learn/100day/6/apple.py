"""
请说出下面的方程有多少组正整数解。
x_1 + x_2 + x_3 + x_4 = 8
事实上，上面的问题等同于将8个苹果分成四组每组至少一个苹果有多少种方案
"""
m = int(input("共有几个苹果"))
n = int(input("分几组"))
f_m = 1
for num in range(1, m+1):
    f_m *= num
f_n = 1
for num in range(1, n+1):
    f_n *= num
f_mn = 1
for num in range(1,m-n+1):
    f_mn *= num
print(f_m/(f_n*f_mn))

