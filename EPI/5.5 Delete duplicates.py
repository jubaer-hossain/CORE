# Sliding window technique

# O(n) time | O(1) space
def deleteDuplicates(array):
    if not array: # Empty array
        return 0

    vacantIdx = 1

    for i in range(1, len(array)):
        # This is a NOT pattern. We are only performing the swap
        # When we see the next UNIQUE number.
        # We are assuming that next number will be by default a duplicate
        print("i = ", i, " writeIdx = ", vacantIdx)
        print(array)
        if array[vacantIdx - 1] != array[i]: 
            array[vacantIdx] = array[i]
            vacantIdx += 1

    return array[:vacantIdx]


a = [2, 5, 5, 5, 7, 7, 8]
# [2, 5, 7, 8, 9]
print(deleteDuplicates(a))


# Have a writeIdx = 1 and iterator i = 1
# When the value of A[writeIdx - 1] != A[i] we found a new Unique element
# We overwrite the current A[writeIdx] to A[i], the newly found Unique element

# O(n) time | O(1) space
def deleteDuplicatesTwo(A):
    if not A:
        return 0

    writeIdx = 1 # The next idx to write an Unique value

    for i in range(1, len(A)):
        if A[writeIdx - 1] != A[i]:
            A[writeIdx] = A[i]
            writeIdx += 1

    return A[:writeIdx]

a = [2, 5, 5, 5, 7, 7, 8]
# [2, 5, 7, 8, 9]
print(deleteDuplicatesTwo(a))