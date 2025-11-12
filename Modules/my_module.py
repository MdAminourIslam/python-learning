pi = 3.14156

def square(x):
    return x **2

def sum(*args):
    s = 0
    for arg in args:
        s += arg
    return s

def cube(x):
    return x ** 3

def area(r):
    return pi * r * r

def binarySearch(nums, x):
    lo = 0
    hi = len(nums) - 1
    nums.sort()
    while lo <= hi:
        mid = int((lo + hi) / 2)

        if (nums[mid] == x):
            return (f"Element {x} if Found at index {mid}")
            return
        elif (nums[mid] > x):
            hi = mid - 1
        else:
            lo = mid + 1
    return (f"Element {x} is Not Found!!")


def isPalindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def fatorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    
    return res
