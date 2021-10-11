from collections import deque

q = deque(['eric', "jeff", "nathan"])

q.append("Jubaer")
q.popleft()
print(q)

print()
squares = [x**2 for x in range(10)]

cubes = [x ** 2 for x in range(15)]

set = [(x, y) for x in [1, 3, 4] for y in [4, 5, 6] if x != y]

print(set)

#touples

touple1 = 1, 3, 'Jamil' #Main difference is there is no square brackets

print(touple1)

touple2 = touple1, 'Lalli', 2, 1660

print('\n', touple2)

#Touples are immutable but they can contain mutable objects like arry or vectors

#Single touple contains a comma at the end

singleton = 'hello',