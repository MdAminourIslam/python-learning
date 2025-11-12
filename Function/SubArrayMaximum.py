def subArrayMaxSum(nums, n):
    mx = nums[0]
    cur_sum = 0
    for i in range(n):
        cur_sum += nums[i]
        if cur_sum < 0:
            cur_sum = 0
        
        mx = max(mx, cur_sum)
    return mx


n = int(input("Enter Size of List : "))
nums = []

for i in range(n):
    num = int(input(f"Enter {i}th Element : "))
    nums.append(num)

mxSum = subArrayMaxSum(nums, n)
print(f"Max subArray sum is : {mxSum}")
