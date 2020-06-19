"""跑马灯"""

import os
import time

def main():
    content = "北京欢迎您"
    while True:
        os.system('cls')
        print(content)
        time.sleep(1)
        content = content [1:]+content[0]

if __name__ == '__main__':
    main()    