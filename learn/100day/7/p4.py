"""冒泡排序法"""

def sort_max(x):
    for i in range(len(x)-1):
        for j in range(len(x)-i-1):
            m1 = x[j]
            m2 = x[j+1]
            if m1 < m2:
                x[j],x[j+1] = m2, m1
    print(x)

def max2(x):
    """第一、第二最大值"""
    m1, m2 = x[0], x[1] if x[0]>x[1] else (x[1], x[0])
    for index in range(2, len(x)-1):
        if x[index] > m1:
            m1, m2 = x[index], m1
        elif x[index] > m2:
            m2 = x[index]
    return m1,m2

if __name__ == '__main__':
    
    sort_max([1,2,3,6,8,4])
    print(max2([1,2,3,6,8,4]))