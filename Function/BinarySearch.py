def binarySearch(nums, n, x):
    lo = 0
    hi = n - 1
    while lo <= hi:
        mid = int((lo + hi) / 2)

        if (nums[mid] == x):
            print(f"Element {x} if Found at index {mid}")
            return
        elif (nums[mid] > x):
            hi = mid - 1
        else:
            lo = mid + 1
    print(f"Element {x} is Not Found!!")


n = int(input("Enter Size of List : "))

nums = []

for i in range(n):
    num = int(input(f"Enter {i}th Element : "))
    #nums.append(int(input(f"Enter {i}th Element : "))) #This is also work
    nums.append(num)

x = int(input("Enter Search Element : "))

nums.sort()
#print(nums)

binarySearch(nums, n, x)