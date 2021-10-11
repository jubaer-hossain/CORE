# In-place swapping of two numbers
x, y = 10, 20
print(x, y)
x, y = y, x
print(x, y) # Output: 20 10

# Reverseing a string in python
a = "FooBar"
print("The reverse is: ", a[::-1]) # arrayName[startIndex : endIndex : Order]

# Create a single line from all elements of the list
companies = ["Apple", "Google", "Microsoft"]
print(" ".join(companies))

# Chaining comparison operator
n = 10
result = 1 < n < 20
print(result) # True
result = 1 < n <= 9
print(result) # False

# Return multiple valued from functions
def function():
    return 1, 2, 3, 4

a, b, c, d = function()
print(a, b, c, d) # 1 2 3 4

# Find most frequent value in a list
nums = [1, 3, 4, 3, 4, 4, 3, 3, 5, 5, 7, 4, 2, 3, 4]
print(max(set(nums), key = nums.count)) # Output: 3

# Check the memory use of an object
import sys
x = 100
print(sys.getsizeof(x)) # 28, usually an int occupies 28 - 32 bytes in memory

# Check if two strings are anagram or not
    # Method one: using Counter. O(n)
from collections import Counter
def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2) # True or False

    # Method two: using sorting. (nlogn)
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2) # True or False. Here sorted() is a function that compares the sorted version of a list or string but does not sort the entire list
