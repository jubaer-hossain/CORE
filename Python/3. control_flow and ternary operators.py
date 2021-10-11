x = int(input("Please enter an int: "))

if x < 0:
    print("X is less than zero")
elif x > 0:
    print("Greater than zero")
else:
    print("Zero is the perfect number")

words = ['cats', 'dogs', 'tiger', 'lion']

num1 = 10
num2 = 20

print(num1 if num1 > num2 else num2) # Output: 20. Basically a whole if else in one line
