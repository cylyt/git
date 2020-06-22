"""约瑟夫环"""

def main():
    persons = [True]*30
    check_num,counter, index = 0, 0, 0
    while counter < 15:
        if persons[index]: 
            check_num += 1
            if check_num  == 9:
                persons[index] = False
                check_num = 0 
                counter += 1
              
        index += 1
        index %= 30
        print(persons)


    

if __name__ == '__main__':
    main()