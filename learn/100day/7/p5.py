"""计算指定的年月日是一年的第几天"""

def is_leap_year(year):

    return year % 4 == 0 and year % 100 !=0 or year % 400 == 0
 

def which_day(year,month,day):

    day_of_month = [[31,28,31,30,31,30,31,31,30,31,30,31],
    [31,28,31,30,31,30,31,31,30,31,30,31]][is_leap_year(year)]

    total_day = 0
    for index in range(month-1):
        total_day += day_of_month(index)
    total_day += day
    return total_day
        

if __name__ == '__main__':
    year = int(input("输入年份"))
    month = int(input("输入月份"))
    day = int(input("输入天"))
    

    print(which_day(year,month,day))

