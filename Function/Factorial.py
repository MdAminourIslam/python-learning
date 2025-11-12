def fatorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    
    return res


n = int(input(f"Enter a Number : "))

result = fatorial(n)
print(f"Factorial of {n} is {result}")