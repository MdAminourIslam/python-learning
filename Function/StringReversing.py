def stringReverse(s):
    s = list(s)  # convert string to list to allow swapping
    i = 0
    j = len(s) - 1
    while i < j:
        ch = s[i]
        s[i] = s[j]
        s[j] = ch
        i += 1
        j -= 1
    return ''.join(s)  # convert list back to string

name = input("Enter Your Name: ")
print("Reversed Name: " + stringReverse(name))
