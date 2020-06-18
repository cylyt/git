def gcd(x, y):
    """最大公约数"""
    if x > y:
        x, y = y, x
    for factor in range (x,0,-1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x, y):
    """最小公倍数"""
    return x * y // gcd(x, y)

def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True if num != 1 else False

if __name__ == '__main__':
    num = int(input("请输入正整数"))
    if is_palindrome(num) and is_prime(num):
        print("%d是回文素数" %num)