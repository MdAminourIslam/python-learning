# Python List Comprehension হল একটি ছোট, 
# সুন্দর ও শক্তিশালী পদ্ধতি যা দিয়ে আমরা একটি নতুন 
# list তৈরি করতে পারি এক লাইনে, 
# for loop এবং if condition ব্যবহার করে।

# Basic Syntax:
# new_list = [expression for item in iterable]
# new_list = [expression for item in iterable if condition]


nums = [i for i in range(10)] 
nums = [i for i in range(10) if i % 2 == 0]

nums = [1, -1, 2, -4, 2, -33, 4, -55]
positive_nums = [num for num in nums if num >= 0]
negative_nums = [num for num in nums if num < 0]

print(negative_nums)


