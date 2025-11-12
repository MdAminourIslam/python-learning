#LEGB
#Local → Enclosing → Global → Built-in

num = 100 #Global variable
def myfunc0():
    global num
    num = 10
    return num

print(myfunc0())
print(num)
