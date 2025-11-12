import my_module as mm

print(mm.pi)
print(mm.square(2))
print(mm.cube(2))
print(mm.sum(2, 4, 4))
print(mm.area(2))

print(mm.binarySearch([1, 2, 3, 4], 2))
print(mm.binarySearch([1, 3, 4, 2], 2))
print(mm.binarySearch([1, 3, 4, 2], 6))

print(mm.isPalindrome("Rahim"))
print(mm.isPalindrome("madam"))

# print(dir(mm))
# print(help(mm))

print(f"Factorial of 4 = {mm.fatorial(4)}")