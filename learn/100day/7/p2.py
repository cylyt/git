"""验证码"""

import random

def generate_code(code_len = 4):
    all_chars='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars)-1
    code = ""
    for _ in range (code_len):
        index = random.randint(0,last_pos)
        code += all_chars[index]
    return code

if __name__ == '__main__':
    code_len = int(input("输入验证码长度"))
    code = generate_code(code_len)
    print(code)
