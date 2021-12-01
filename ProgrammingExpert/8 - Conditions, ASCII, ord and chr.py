# Comparing strings
str1 = "ABc" 
str2 = "ABC"

cond = str1 < str2 # Fales, because "c" ASCII value is greater than "C"
print(cond)

print(ord("a")) # 97
print(chr(97)) # a

# Some weird comparisons
cond = False == 0 # True
cond = True == 1 # True
cond = False == "" # False, because they are different types
cond2 = True == "True" # False, because they are different types