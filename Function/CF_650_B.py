def evenArray():
    n = int(input())
    cntEven = 0
    cntOdd = 0
    a = list(map(int, input().split()))

    for x in a:
        if (x % 2 == 0) :
            cntEven += 1
        else:
            cntOdd += 1
    
    requireOdd = int(n / 2)
    requiredEven = n - requireOdd

    if cntOdd != requireOdd or cntEven != requiredEven:
        print(-1)
    else:
        cnt = 0
        for i in range(0, n):
            if (a[i] % 2) != (i % 2):
                cnt += 1
        
        print(int(cnt / 2))


tc = int(input())
while tc > 0:
    evenArray()
    tc -= 1