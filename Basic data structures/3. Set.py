setOne = {1, 2, 3, 4, 5}
setTwo = {5, 6, 7, 8, 9, 9, 10} # A set can not contain duplicates. So this will automatically be: {5, 6, 7, 8, 9}
print(setTwo)

len(setOne) # 5

5 in setOne # True

12 not in setOne # True

print(setOne.isdisjoint(setTwo)) # Because setOne and setTwo has one element in common

# Subset functions. Superset is basically the opposite sign
subSetOne = {2, 3, 5}

print(subSetOne.issubset(setOne)) # True
if subSetOne <= setOne:
    print("'subSetOne' is a Subset of 'setOne'")
if subSetOne < setOne: # subSetOne <= setOne and subSetOne != setOne
    print("'subSetOne' is a proper subset of 'setOne'")

# Union
newSuperSet = setOne | setTwo # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
newSuperSetTwo = setOne.union(setTwo) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(newSuperSet)
print(newSuperSetTwo)

# Intersection
commonElements = setOne & setTwo # {5}
commonElementsTwo = setOne.intersection(setTwo) # {5}
print(commonElements, commonElementsTwo)

# Difference: Basically subtraction. Returns a new set with elements in the set that are not in the others
differenceSet = setOne - setTwo # {1, 2, 3, 4}
differenceSetTwo = setOne.difference(setTwo) # {1, 2, 3, 4}
print(differenceSet, differenceSetTwo)

# Symmetric_difference: Elements present in either sets but not in both sets
symmetricSet = setOne ^ setTwo # {1, 2, 3, 4, 6, 7, 8, 9, 10}
symmetricSetTwo = setOne.symmetric_difference(setTwo) # {1, 2, 3, 4, 6, 7, 8, 9, 10}
print(symmetricSet, symmetricSetTwo)

# Copying a set
copiedSet = setOne.copy() # {1, 2, 3, 4, 5}
copiedSetTwo = setOne # {1, 2, 3, 4, 5}
print(f'Copied sets are: {copiedSet}, {copiedSetTwo}')

# update(): Update the set keeping all the elements found in it and in other sets
setFour = {12}
setFour |= setTwo # {5, 6, 7, 8, 9, 10, 12}
print(setFour)

# intersection_update(): Update the current set taking only the common elements from all the sets
setFive = {9}
setFive &= setTwo # {9}
print(setFive)

# difference_update(): Update the set removing elements found in others
setSix = {5}
setSix -= setOne # {1, 2, 3, 4}

# symmetric_difference_update(): Update the current set with elements that are commoon in either set but not in both sets
setSeven = {5, 6}
setSeven ^= setOne # {1, 2, 3, 4, 6}

# Some common & self explanatory methods
setOne.add(8) # {1, 2, 3, 4, 5, 8}
setOne.remove(5) # {1, 2, 3, 4, 8} -> Raises a KeyError if the element is not present
setOne.discard(10) # Remove an element if it is present
setOne.pop() # Remove and Return an arbitrary element from the set. Raises KeyError if the set is empty
set.clear() # Removes all elements