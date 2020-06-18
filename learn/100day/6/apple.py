"""
请说出下面的方程有多少组正整数解。
x_1 + x_2 + x_3 + x_4 = 8
事实上，上面的问题等同于将8个苹果分成四组每组至少一个苹果有多少种方案
"""
def fac(num):
    result = 1
    for n in range(1,num+1):
        result *= n
    return result

m = int(input("共有几个苹果"))
n = int(input("分几组"))
f_m = 1

print(fac(m)/(fac(n)*fac(m-n)))

