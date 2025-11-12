def isPalindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return "Not Palindome"
        i += 1
        j -= 1
    return "Palindome"

name = input("Enter Your Name : ")

print(f"{name} is {isPalindrome(name)}")