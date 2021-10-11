print("hello world")
character_name = "John"
character_age = 35
is_male = True

print("My name is " + character_name)

# working with string

print("My name is Jubaer\nMy age is 25")
print("This is my quotation\"")

string = "This is a string"

print(string)

another_string = "This is another string"

print(string + another_string)

# convert to lowercase

print(string.lower().islower())

print(len(string))

print(string[0]) # prints first character of the string

print(string.index("T")) # returns the first index of the character

print(another_string.index("anot")) # returns where "anot" starts within the string

print(string.replace("string", "good string")) # replace part of string with something else

print("\n\nWORKING WITH NUMBERS")
# Using numbers in python #

print(2 * (5 + 10))
print(10 % 3)

my_num = -5 

# convert a number to string

print(str(my_num))

print(str(my_num) + " Python can't print numbers with a string at the beginning of the sentence")

print(abs(my_num))

print(pow(2, 4))

print(max(10, 20))

from math import * # Whoa you can import headers in the middle of the code!!!

print(round(3.5)) # rounds to ceil value

print(floor(abs(-3.5)))

print("\n\nGETTING INPUT FROM USER")
# User input in python #

# name = input() # python 2.7 doesn't have the input() function

# print(name)
num1 = input("enter a number")
num2 = input("enter another number")

print(float(num1) + float(num2))