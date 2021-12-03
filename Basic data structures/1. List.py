arr = [1, 2, 3, True, 3.4, "Hello", 2]
arr.append(12) # [1, 2, 3, True, 3.4, "Hello", 12]

lastElement = arr.pop() # [1, 2, 3, True, 3.4, "Hello"]
print(lastElement) # 12

frequency = arr.count(2) # 2

idx = arr.index(2) # 1, because 2 exist in position 1

if(2 in arr): print("2 is present in the list")

# Add list
brr = [9, 10, 11]

listThree = arr + brr # New list with two elements

arr.extend(brr) # arr = [1, 2, 3, True, 3.4, 'Hello', 2, 9, 10, 11]
print(arr)

# Nested list
listFour = [[1, 2, 3, [100, 200, 300]], (12, 11), [23, 11], [45], "hello"]
print(listFour[0]) # [1, 2, 3, [100]]
print(listFour[1]) # (12, 11)
print(listFour[1][0]) # 12
print(listFour[0][3]) # [100, 200, 300]
print(listFour[0][3][2]) # 300
