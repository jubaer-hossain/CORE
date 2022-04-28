"""
Algorithm:
1. Compare the lengths and first values of the arrays cause they are the roots
2. Get all smaller values and all greater & equal values in two new arrays for each array
3. Call the recursive function on left subtree passing in the smaller values
and on the right subtree passing in the larger values to validate those two
Sub-BSTs

Base-case: When both arrays are empty, return True
"""

# O(n^2) time | O(n^2) space 
# Because we are traversing the array N times
# And each time we are going through N values and storing N values in new array
def sameBsts(arrayOne, arrayTwo):
    return validateBSTs(arrayOne, arrayTwo,)

def validateBSTs(arrayOne, arrayTwo, ):
    if len(arrayOne) != len(arrayTwo):
        return False
    
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True
    
    if arrayOne[0] != arrayTwo[0]:
        return False
    
    leftSubtreeValuesOfArrayOne = getSmallerValues(arrayOne)
    rightSubtreeValuesOfArrayOne = getGreaterOrEqualValues(arrayOne)

    leftSubtreeValuesOfArrayTwo = getSmallerValues(arrayTwo)
    rightSubtreeValuesOfArrayTwo = getGreaterOrEqualValues(arrayTwo)
    
    return validateBSTs(leftSubtreeValuesOfArrayOne, leftSubtreeValuesOfArrayTwo) and validateBSTs(rightSubtreeValuesOfArrayOne, rightSubtreeValuesOfArrayTwo)

def getSmallerValues(array):
    smaller = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
    return smaller

def getGreaterOrEqualValues(array):
    greaterOrEqual = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            greaterOrEqual.append(array[i])
    return greaterOrEqual

"""
Algorithm:
1. In each recursive call we pass rootIdxOne and rootIdxTwo
2. Then calculate next smaller value and next larger value
3. Then pass those new values as tree roots to validate 
if the left and right segmenets are true

Base-case: rootOneIdx or rootTwoIdx becomes -1, we need to check if
both of them are -1(return rootOneIdx == rootTwoIdx). Otherwise we will face
Index Error, by trying to access -1 index from any of those arrays
"""
# O(n^2) time | O(h) space
def sameBsts(arrayOne, arrayTwo):
    return validateBSTs(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf") )

def validateBSTs(arrayOne, arrayTwo, rootIdxOne, rootIdxTwo, minValue, maxValue):
    if rootIdxOne == -1 or rootIdxTwo == -1:
        return rootIdxOne == rootIdxTwo
    
    if arrayOne[rootIdxOne] != arrayTwo[rootIdxTwo]:
        return False

    leftRootIdxOne = getSmallerValue(arrayOne, rootIdxOne, minValue)
    rightRootIdxOne = getGreaterOrEqualValue(arrayOne, rootIdxOne, maxValue)

    leftRootIdxTwo = getSmallerValue(arrayTwo, rootIdxTwo, minValue)
    rightRootIdxTwo = getGreaterOrEqualValue(arrayTwo, rootIdxTwo, maxValue)

    currentValue = arrayOne[rootIdxOne]
    
    return validateBSTs(arrayOne, arrayTwo, leftRootIdxOne, leftRootIdxTwo, minValue, currentValue) and validateBSTs(arrayOne, arrayTwo, rightRootIdxOne, rightRootIdxTwo, currentValue, maxValue)

def getSmallerValue(array, startIdx, minValue):
    for i in range(startIdx + 1, len(array)):
        if array[i] < array[startIdx] and array[i] >= minValue:
            return i
    return -1

def getGreaterOrEqualValue(array, startIdx, maxValue):
    for i in range(startIdx + 1, len(array)):
        if array[i] >= array[startIdx] and array[i] < maxValue:
            return i
    return -1