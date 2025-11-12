
def arrayMin(nums):
    mn = nums[0]
    for num in nums:
        mn = min(mn, num)

    """else: 
        return Min //This is Muti-Line Comment
    """
    return mn


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mn = arrayMin(nums)

print(f"Min is {mn}")
