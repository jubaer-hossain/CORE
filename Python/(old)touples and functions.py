coordinates = (4, 5)

# coordinates[1] = 10 # this doesn't modify the 

touple_list = [(1, 2), (4, 5), (8, 9)]

print(coordinates[1])

print(touple_list)

def hello(name):
    print("Hello " + name)

hello("Avocado")

def cube(num):
    return num * num * num

print(cube(3))

is_male = True

is_tall = False

if is_male and is_tall:
    print("You are a male")
elif is_male and not(is_tall):
    print("Something else")
else:
    print("You are not a male")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(4, 12, 33))