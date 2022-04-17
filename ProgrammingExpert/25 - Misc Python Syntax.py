# List comprehensions
arr = [i / 2 for i in range(1, 11) if i % 2 == 0] # arr = [1.0, 2.0, 3.0, 4.0, 5.0]

# Nested loops in list comprehensions
brr = [i * j for i in range(0, 3) for j in range(5)] # brr = [0, 0, 0, 0, 0,   0, 1, 2, 3, 4,   0, 2, 4, 6, 8]
print(brr)

# For touples. You need to convert the list into touple
crr = tuple([i for i in range(5)])

# Set comprehension: No duplicates
set1 = {i * j for i in range(4) for j in range(4)} # set1 = {0, 1, 2, 3, 4, 6, 9}. No duplicates
print(set1)

# Dictionary comprehension: key, value pair
dict1 = {i : j for i in range(8) for j in range(12)} # dict1 = {0: 11, 1: 11, 2: 11, 3: 11, 4: 11, 5: 11, 6: 11, 7: 11}. Because every neseted loop the value gets updated and we are only seeing the last value of "j" after the loop finishes
print(dict1)

# Multiple variable assignment
x = y = z = 1 # All have value 1
x, y, z = 1, 2, 3

# Unpacking
x, y = (1, 2) # x = 1, y = 2. This tuple is unpacked and assigned to x and y
x, y, z = [1, 3, 4] # For list

arr = [i for i in range(3)] # arr = [0, 1, 2]
a, b, c = arr # a = 0, b = 1, c = 2

# docstring
def foo():
    """
    This is the description of the function
    """
    pass

help(foo) # Prints the Documentation String of the function. Works for native functions as well
help(len)

a = max(1, 3, 4, 5) # a will be 5