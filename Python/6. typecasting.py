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