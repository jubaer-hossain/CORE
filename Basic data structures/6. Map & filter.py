listOne = [1, 2, 3, 4, 5]
listTwo = map(lambda x: x ** 2, listOne) # Returns a map iteratable object. Still can loop through it
listTwo = list(map(lambda x: x ** 2, listOne)) # Converts to a list

listThree = [[1, 2], [2, 3, 5], [12, 33], [4]]
listFour = list(map(lambda x: sum(x), listThree))
print(listFour) # [3, 5, 45, 4]

listFive = filter(lambda x: sum(x) > 6, listThree) # Returns a filter iteratable object. Can loop
listFive = list(filter(lambda x: sum(x) > 6, listThree)) # [[2, 3, 5], [12, 33]]
print(listFive)

listSix = list(filter(lambda x: len(x) > 2 and sum(x) > 6, listThree)) # [[2, 3, 5]]
print(listSix)

# Map and Filter at the same time
listSeven = filter(lambda y: y % 2 == 0, map(lambda x: sum(x), listThree)) # Only taking sum that are even
print(list(listSeven)) # [10, 4]