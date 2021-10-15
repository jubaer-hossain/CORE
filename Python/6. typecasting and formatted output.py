# Example-1: We can take string input but convert them to int and perform arithmatic operation
num1 = input("Enter number-1: ")
num2 = input("Enter number-2: ")

sum = int(num1) + int(num2)
print("The sum is:", sum)

# But this method is not good practice if you want to perform lots of arithmatic operations
# Example-2: We can directly take integer input like this
num3 = int(input("Enter number-3: "))
num4 = int(input("Enter number-4: "))

result = num3 + num4
print("The result is:", result)

sum = num3 + num4
print("The sum is:", sum)

# Finding the type of a variable
print(type(sum)) # <class 'int'>

# Output formated multiple ints
print(f"{num1} + {num2} = {num1 + num2}") # Output: 11 + 11 = 1111. Because we haven't typecasted it to int
print(f"{num1} + {num2} = {int(num1 + num2)}") # Output: 11 + 11 = 1111. Because we need to typecast to to individual variables
print(f"{num1} + {num2} = {int(num1) + int(num2)}") # Output: 11 + 11 = 22

# Static typing in functions
# The following function takes string variable called name as input and the return type is string
def greetings(name: str) -> str:
    return "Hello" + name

# We can also define new types and strickly limit a functions input and return type of that specific type
from typing import NewType
userId = NewType("userId", int) # Defining a new type
some_id = userId(122)

def getUserName(user_id: userId) -> str:
    ...

# Typechecks
user_a = getUserName(userId(122))

# Does not typechecks; an int is not a userId
user_b = getUserName(12)

# Read more about Typing in python here: https://docs.python.org/3/library/typing.html
