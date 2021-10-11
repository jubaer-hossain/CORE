# Input a line as seperated integers
lineInput = input()
arr = list(lineInput.split()) # List of string numbers
print(arr) # ['1', '12', '3'] etc as string
print(arr[0] + arr[1]) # Will not give arithmatic results
print(int(arr[0]) + int(arr[1])) # Will give regular arithmaric result

# Convert a line of string into an integer array
lineInput = lineInput.split() # Converting line into array of strings -> ['1', '12', '3'] etc as string
print(lineInput)
brr = [int(i) for i in lineInput]
print(brr) # This will output as integer array -> [1, 3, 5] etc

# Split a number into integer digits
numberString = input()
digits = [int(i) for i in numberString]
print(digits) # If we input 123 as string it will output [1, 2, 3] as int array

# Delimiter -> This could be useful for string seperation where we have full stop
str = input()
sentences = str.split('.') # Basically seperate where it finds a fullstop
print(sentences)