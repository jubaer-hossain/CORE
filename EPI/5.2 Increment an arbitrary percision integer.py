# O(2n) time | O(1) space
def plusOne(array):
    carry = 1
    for i in reversed(range(len(array))): # O(n)
        if array[i] != 9:
            array[i] += 1
            carry = 0
            break
        else:
            array[i] = 0
    
    if carry == 1:
        array.insert(0, 1) # O(n) Inserting 1 at 0th index and pushing all elements back

    return array

print(plusOne([1, 9, 9]))
print(plusOne([0]))
print(plusOne([1, 2, 9]))