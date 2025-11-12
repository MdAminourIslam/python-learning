def fibo(n):
    a = 0
    b = 1
    if n < 2:
        return n
    for i in range(2, n + 1):
        fiboi = a + b
        a = b 
        b = fiboi
    return b


n = int(input("Enter a number : "))
print(F"Fibo of {n} = {fibo(n)}")