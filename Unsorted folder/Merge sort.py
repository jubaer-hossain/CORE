# O(nlog(n)) Time | O(nlog(n)) Space
"""
Total complexity = mergeSort(N)       + merge(N)
                 = mergeSort(8)       + merge(8)
                 = mergeSort(4) + mergeSort(4) + merge
                 = 2 * mergeSort(N/2) + N
                 = 2 * mergeSort(8/2) + 8
                 = 2 * mergeSort(4) + 8 -> 2 * 8 + 8 => 24 (8 * log(8))
                 = 2 * mergeSort(2) + 4 -> 2 * 2 + 4 => 8
                 = 2 * mergeSort(1) + 2 -> 2
                 = 2 * 0 + 2

                 [6, 5]
                 [6], [5]
                 [5, 6]
"""
def mergeSort(array):
    if len(array) == 1:
        return array
    middleIdx = len(array) // 2
    leftHalf = array[:middleIdx]
    rightHalf = array[middleIdx:]

    return merge(mergeSort(leftHalf), mergeSort(rightHalf))

def merge(leftHalf, rightHalf):
    sortedArray = [None] * (len(leftHalf) + len(rightHalf))
    k = i = j = 0

    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            sortedArray[k] = leftHalf[i]
            i += 1
        else:
            sortedArray[k] = rightHalf[j]
            j += 1
        k += 1

    while i < len(leftHalf):
        sortedArray[k] = leftHalf[i]
        i += 1
        k += 1
    while j < len(rightHalf):
        sortedArray[k] = rightHalf[j]
        j += 1
        k += 1
    return sortedArray # New array, not the original array


# O(nlog(n)) Time | O(n) Space. O(n + log(n)) Space precisely becuase of the recursive calls
def mergeSort(array):
    if len(array) <= 1:
        return array

    auxiliaryArray = array[:]
    mergeSortHelper(array, 0, len(array) - 1, auxiliaryArray)
    return array

""" 
The Main and Auxiliary Array switching visualiztaion:
M(8) -> A -> M -> A
M(9) -> A -> M -> A -> M
M(16) -> A -> M -> A -> M
"""
def mergeSortHelper(mainArray, startIdx, endIdx, auxiliaryArray):
    if startIdx == endIdx:
        return
    middleIdx = (startIdx + endIdx) // 2
    mergeSortHelper(auxiliaryArray, startIdx, middleIdx, mainArray)
    mergeSortHelper(auxiliaryArray, middleIdx + 1, endIdx, mainArray)
    merge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray)

def merge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray):
    k = startIdx
    i = startIdx
    j = middleIdx + 1

    while i <= middleIdx and j <= endIdx:
        if auxiliaryArray[i] <= auxiliaryArray[j]:
            mainArray[k] = auxiliaryArray[i]
            i += 1
        else:
            mainArray[k] = auxiliaryArray[j]
            j += 1
        k += 1

    while i <= middleIdx:
        mainArray[k] = auxiliaryArray[i]
        i += 1
        k += 1
    while j <= endIdx:
        mainArray[k] = auxiliaryArray[j]
        j += 1
        k += 1