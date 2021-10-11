print("hello programming!")

num = 5

if num < 5:
    print("Lalala number")
else:
    print("not a lalala number")

print(10 * 10)
print(17 / 3) #Returns a float number
print( 17 // 3) #Returns the floor value
print(17 % 3 )
print(5 ** 3) #Basically 5 ^ 3
print(3.5 * 3 - 1)

str = r'first line \nSecond line' #for raw string

str2 = ' Third string'

print(str + str2) #concate
print(str * 3 + str2) #concate & multiply

message = ('This is a new message'
            ' The second part of the message ' + str)
print(message)

language = 'Python'

print(language[1:3])
print(language[3:5])

print(len(language))

squares = [1, 4, 9, 16]

print(squares[1])

print(squares[0:1])

squares.append(7 ** 2)

print(squares)

letters= ['a', 'b', 'c', 'd', 'e', 'f']

print(letters)
print("After modification:\n")
letters[2:5] = ['C', 'D', 'E']

print(letters)

#2D array with python

# a = [1, 2, 3]
# b = ['a', 'b', 'c']

# x = [a, b]
# print(x)

# printing a specific index of a 2D array
# print(x[1][0]) #Row first and then column

print("\nPrinting Fibonacci series")

a, b = 0, 1

while a < 100:
    print(a)
    # a, b = b, a+b -> Here a+b is calculated first and then the values get assigned
    c = a + b
    a = b
    b = c