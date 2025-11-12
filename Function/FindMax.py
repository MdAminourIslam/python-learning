
def arrayMax(nums):
    mx = nums[0]
    for num in nums:
        mx = max(mx, num)

    """else: 
        return Max //This is Muti-Line Comment
    """
    return mx


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mx = arrayMax(nums)

print(f"Max is {mx}")
