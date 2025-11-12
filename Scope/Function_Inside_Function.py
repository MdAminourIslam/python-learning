def myfunc1():
    x = "Hi" # Local Variable
    def myfunc2(): # Inner Function
        nonlocal x
        x = "hello"
    myfunc2()
    return x


#print(myfunc1())

x = 2
def outer():
    x = 5
    def inner():
        x = 10
        print("Inner:", x)
    inner()
    print("Outer:", x)

outer()
print("Global:", x)


