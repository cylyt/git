def test_1():
    return 100*100

def test_2():
    x=[]
    for i in range(10000):
        temp=i/1000.0
        x.append(temp*temp)
    return x

def test_3(condition=False):
    if condition:
        test_3()

if __name__=="__main__":
    a=test_1()
    b=test_2()
    c=test_3(True)