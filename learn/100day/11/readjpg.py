def main():
    try:
        with open('D:\\0.jpg', 'rb') as fs1:
            date = fs1.read()
            print(type(date))
        with open('D:\\1.jpg', 'wb') as fs2:
            fs2.write(date)
    except FileNotFoundError as e:
        print('指定文件无法打开')
    except IOError as e:
        print('读写文件出现错误')
    print('程序执行结束')

if __name__ =='__main__':
    main()