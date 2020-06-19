def get_suffix(filename):
    pos = filename.find('.')
    if 0 < pos < len(filename)-1:
        index = pos
        return filename[index:]
    else:
        return""

if __name__ == '__main__':
    filename = str(input("文件名"))
    suffix = get_suffix(filename)
    print(suffix)