def initial_number(x):
    print("1. Initial number"
            "(orig environment during function creation):{}".format(x))

    def modified_number(y):
        print("X:{},y:{},x+y:{}".format(x,y,x+y))

    return modified_number

if __name__=='__main__':
    foo=initial_number(100)
    print("2. Now calling this function with"
            "its origianl environment loaded:")
    foo(1)
    foo(5)