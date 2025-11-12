import math

num1 = 10
num2 = 3

#Multi-Line Comment
'''
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print(int(num1 / num2))

print(round(num1 / num2, 2))
'''

num = 3.4

result = math.pow(num, 2)
result = math.ceil(num)
result = math.floor(num)
result = int(math.sqrt(num1))
result = float(math.sqrt(num1))
result = round(math.sqrt(num1), 4)
result = round(num, 4) # This give 3.4, not 3.4000

result = math.gcd(num1, 5, 20)
#gcd function find gcd of n numbers

result = math.lcm(num2, num1, 4) #lcm of n numbers
result = (2 ^ 4)
# result = math.pow(2, 3)
print(result)


