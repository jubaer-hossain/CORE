char = "A"
name = "Jubaer"

# Checks if a character is alpha-numeric
print(char.isalnum()) # True

# Checks if a character is upper or lower case
print(char.isupper()) # True
print(char.islower()) # False

print("Name is lower: ", name.islower()) # False cause the first character is not lower
print("Converting name to all lower: ", name.lower()) # jubaer

# Converts a chacater into upper or lower case but DOES NOT modify the original character
print(char.lower()) # a
print(char) # A