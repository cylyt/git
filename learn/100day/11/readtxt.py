def main():
    f = None
    try:
        with open('D:\ABC.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定文件')
    finally:
        if f:
            f.close()
    
    with open('D:\ABC.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)

if __name__ == '__main__':
    main()