i = 0
while i < 10:
    i += 1
    if i == 5:
        continue # Basically continue skips the rest of the loop commands on that iteration
    print(i)

# For loop
print("\nFor loop")
arr = list(range(12, 22)) # Generates an array of lengh 10 from 12 to 21

for value in arr: # Here value is the actual value of the elements in each iteration
    print(value)

print("\nRegular C++ for loop with range:")
for i in range(10):
    print(arr[i])

print("\nReversed range:")
for i in reversed(range(10)):
    print(arr[i])