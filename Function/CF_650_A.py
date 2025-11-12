
def shortSubstrings():
    s = input()
    res = ""
    res += s[0]
    res += s[1]
    n = len(s)
    indx = 3
    while indx < n:
        res += s[indx]
        indx += 2
    print(res)
    

n = int(input())
while n > 0:
    shortSubstrings()
    n -= 1