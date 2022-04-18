"""
Given an array and an index i, Rearrange the array so that all the elements less idx i comes first and then equals to i comes next and then greater than i comes last
"""

# Trivial O(n) time and O(n) space solution is using three sub-arrays to store less, equal and greater elements.

"""
Approach-2: O(2n^2) time and O(1) space
1. We start to process the array from start
2. For each element we look for the next smaller element and once we find it, we replace it with current array[i] and break the loop. O(n^2) 
3. We do the same to sort the bigger elements than the pivot but from the end of the array
"""
# O(1) space and O(n^2) time solution
def dutchFlagPartition(pivotIdx, array):
    pivot = array[pivotIdx]

    # First pass: group the elements smaller than pivot
    for i in range(len(array)):
        # Look for a smaller element
        for j in range(i + 1, len(array)):
            if array[j] < pivot: # Everytime we find a smaller element we swap it with array[i] and break
                array[i], array[j] = array[j], array[i]
                break
    
    # Second pass: group the elements greater than the pivot
    for i in reversed(range(len(array))):
        if array[i] < pivot: # No elements is greater than pivot. Pivot is the largest element
            break

        # Look for a larger element and stop when when we reach an elements less than the pivot cause first pass already moved them to the beginning
        for j in reversed(range(len(array))):
            if array[j] > pivot:
                array[i], array[j] = array[j], array[i]
                break


"""
Approach-3: Start from beginning and only swap it with the previous smaller idx. Do this from the end for the larger number as well

We have 4 subarrays: 
bottom(less than the pivot)
middle(equal to the pivot)
unclassified
top(greater than the pivot)

We iterate and place the elements based on their relativeness with the pivot to place them in each group
"""

# O(2n) time and O(1) space
def dutchFlagPartition(pivotIdx, array):
    pivot = array[pivotIdx]

    # First pass: group elements smaller than pivot
    smallerIdx = 0
    for i in range(len(array)):
        if array[i] < pivot:
            array[i], array[smallerIdx] = array[smallerIdx], array[i]
            smallerIdx += 1
    
    # Second pass: group elements larger than pivot
    largerIdx = len(array) - 1
    for i in reversed(range(len(array))):
        if array[i] < pivot: # If current idx is smaller than pivot then break. Because we have already sorted them
            break
        elif array[i] > pivot: # If current element is larger than pivot then swap
            array[i], array[largerIdx] = array[largerIdx], array[i]
            largerIdx -= 1


"""
Approach-4: Each iteration decreases the size of the unclassified elements by 1 and swaps them to smaller or larger group
"""

# O(n) time | O(1) space
def dutchFlagPartition(pivotIdx, array):
    pivot = array[pivotIdx]

    # Keep the following invariants during partitioning:
    # bottom group: array[:smaller]
    # middle group: array[smaller:equal]
    # unclassified group: array[equal:larger]
    # top group: array[larger:]

    smaller, equal, larger = 0, 0, len(array) - 1

    # The target is to have all "equal" idx value equal to the actual pivot. 
    # That is our base point and based on that we will swap smaller or larger numbers
    # And will put them at the beginning or at the end
    while equal < larger:
        if array[equal] < pivot: # Current element should be equal but it is smaller than the pivot
            array[smaller], array[equal] = array[equal], array[smaller]
            smaller += 1
            equal += 1
        elif array[equal] == pivot:
            equal += 1
        else: # array[equal] > pivot
            array[equal], array[larger] = array[larger], array[equal]
            larger -= 1
