
def solve_something():
    a = int(input("Enter a number"))
    b=0
    assert a >0 
    print("Number entered is OK")
    print("Now doing a/b")
    a += a/b
    e = 2*a

def some_function():
    try:
        solve_something()
    except NameError as e:
        print("Name Error...", e.args)
    except AssertionError:
        print("Assertion Error....")
    except Exception as e:
        print("Logging the error")
        raise

if __name__ == "__main__":
    some_function()
