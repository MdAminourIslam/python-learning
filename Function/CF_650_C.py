def helper(cnt, k):
    return int((cnt + k) / (k + 1))

def socialDistance():
    n, k = map(int, input().split())
    s = input()

    if '1' not in s:
        print(helper(n, k))
        return
    
    i = 0
    cnt = 0
    while s[i] != "1":
        i += 1
        cnt += 1
    
    ans = 0
    ans += int(cnt / (k + 1))

    j = n - 1
    cnt = 0
    while s[j] != "1":
        j -= 1
        cnt += 1
    
    ans += int(cnt / (k + 1))

    
    cnt = 0
    while i <= j:
        if s[i] == "0":
            cnt += 1
            if cnt > k:
                ans += 1
                cnt = 0
        else:
            cnt = 0
        i += 1
    
    print(ans)

tc = int(input())
while tc > 0:
    socialDistance()
    tc -= 1