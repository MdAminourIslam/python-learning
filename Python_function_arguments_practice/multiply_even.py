def multiply_even(*args):
    result = 1
    for num in args:
        if num % 2 == 0:
            result *= num
    return result


print(multiply_even(2, 3, 4, 5, 6)) 
print(multiply_even(1, 3, 5, 7))