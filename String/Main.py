#print(help(str)) # Print All string function

"""
Python's string slicing
Slicing allows you to extract parts of a string using this syntax:
string[start:stop:step]

start → index to start (inclusive)
stop → index to stop (exclusive)
step → how many steps to jump
"""

s = "Hello, World!"
result = s[::-1]   # Output: "!dlroW ,olleH"
result = s[:5]     # Output: "Hello"
result = s[7:]     # Output: "World!"
result = s[1:9]    # Output: "ello, Wo"
result = s[-1]     # Last character → "!"
result = s[-5:-1]  # "orld"
result = s[0::2]
result = s[:6]

print(result)