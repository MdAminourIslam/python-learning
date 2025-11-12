# input() — Taking input (always as a string)
# name = input()

# Output: print()
# print(name)

# int(input()) — Taking a number as input
# float(input()) - Taking a Floating number as input

# map(int, input().split()) — Taking multiple numbers from one line
# a , b, c = map(int, input().split())
# print(f"{a} {b} {c}")

# list(map(int, input().split())) — Input as a list of numbers
# nums = list(map(int, input().split()))
# print(nums)

# Formatted output using f-strings
name = "Rasel"
age = 22
print(f"My name is {name} and I am {age} years old.")

# Printing on the same line: use end
for i in range(3):
    print(i, end=' ')


