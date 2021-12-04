# Different ways to declear a dictionary. From the documentation
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)

# Map can have different types as key value
mapOne = {"One": 1, "Two": 4, 5: 8}

listOne = list(mapOne) # Converts map into list of Keys(Not values): ['One', 'Two', 5]
print(listOne) # ['One', 'Two', 5]

del mapOne['One'] # Deletes element that has key = 'One'. New map = {"Two": 4, 5: 8}
len(mapOne) # 2 cause it has two keys

if 'Two' in mapOne:
    print("True") # True because 'Two' exist as a Key

a.clear() # Clears the map

# get(key[, default])
mapOne['Five'] = mapOne.get('Five', 0) + 1 # Basicalley it means -> mapOne['Five'] += 1

# keys()
print(mapOne.keys()) # dict_keys(['Two', 5, 'Five']). dict_keys is a unique type in python
print(list(mapOne.keys())) # ['Two', 5, 'Five'] -> List of keys

# values()
print(mapOne.values()) # dict_values([4, 8, 1]). dict_values is a unique type in python
print(list(mapOne.values())) # [4, 8, 1] -> List of values

# items(): Returns new view of key, value pairs
print(mapOne.items()) # dict_items([('Two', 4), (5, 8), ('Five', 1)]). dict_itmes is a unique type in python
print(list(mapOne.items())) # [('Two', 4), (5, 8), ('Five', 1)] -> List of tuples

# pop(key[, default]): If key is in the dictionary then remove it and return its value, else return default. Else KeyError
print(mapOne.pop('Nine', 'One')) # Because the key 'Nine' is not present in the map so returns 'One'

# popitem(): Remove and return a key, value pair from the dict. Removed in LIFO order from python 3.7
print(mapOne.popitem()) # Returns ('Five', 1) as tuple. Now the dictionary is: {'Two': 4, 5: 8}

# reversed(d): Not clear
reversedMap = reversed(mapOne)
print(reversedMap)

# setdefault(key[, default]): If a key present in the dictionary, return it's value. Else put the key and default value in the dict
mapOne.setdefault('Ten', 1)
print(mapOne) # {'Two': 4, 5: 8, 'Ten': 1}

# Union(|) operator: New in python 3.9
mapTwo = {1: 1, 2: 2, 3: 3}
newMap = mapOne | mapTwo # Will create a new dictionary merging two maps. The second maps keys takes priority if they share keys
print(newMap)

mapOne |= mapTwo # Merges the two maps and updates second maps
print(mapOne)