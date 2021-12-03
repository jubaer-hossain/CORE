# Lambda functions without default
func = lambda x, y, z: x + y + z # If you don't set a default value and give only 3 parameters, it will generate an error

# Lambda with default
funcTwo = lambda x, y, z = 0: x + y + z

print(func(1, 2, 5)) # TypeError. Needs positional argument 'z'
print(funcTwo(2, 3)) # 5 

# 2D sort using a comp method
def comp(arr):
    return arr[1]

listOne = [(1, 2), (1, - 2), (1, -3), (2, -3)]
listTwo = listOne
listOne.sort(key = comp)
print(listOne) # [(1, -3), (2, -3), (1, -2), (1, 2)]

# 2D sort using Lambda
listOne = listTwo
listTwo.sort(key = lambda x: x[1]) # Basically does the same thing as comp() function

# Nested Lambda functions
multiplication = lambda x: lambda y: x * y
res = multiplication(5) # This will return another lambda -> The inner/nested lambda
resTwo = res(5) # Since res is the inner lambda function and have value 'x' already, it will multiply x by y and will RETURN it
print(res(5)) # 25

print(multiplication(5)(4)) # Basically the same thing. Returns 20

# Traditional nested functins
def mul(x):
    def mul2(y):
        return x * y