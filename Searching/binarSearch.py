# O(log(n)) Time | O(1) Space
def binarySearch(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # This is a floor division operator -> //
        potentialMatch = arr[mid]

        if potentialMatch == target:
            return mid
        elif potentialMatch > target:
            right = mid - 1
        elif potentialMatch < target:
            left = mid + 1
    return -1


# O(log(n)) Time | O(n) Space because of the recursive calls
def binarySearchRecursive(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    potentialMatch = arr[mid]

    if target == potentialMatch:
        return mid
    elif target < potentialMatch:
        return binarySearchRecursive(arr, target, left, mid - 1)
    else:
        return binarySearchRecursive(arr, target, mid + 1, right)


# Driver Code
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binarySearch(arr, 7))
print(binarySearchRecursive(arr, 6, 0, len(arr) - 1))
