x = "4"
y = int(x)
print(type(y))

y = int("4") + 4 # 8
z = float(5.5) + 4 # 9.5

y = int(4.5) # Converts into 4
y = int("4.5") # Can not convert string to float

# int to bool
y = bool(" ") # Even a space in string means the string is not empty, hence True
y = bool(4) # True

# Typecasting in input
number = int(input("Enter an int: "))