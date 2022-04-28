# O(n * m) time | O(n + m) space
def multiply(num1, num2):
    if "0" in [num1, num2]:
        return "0"
    
    result = [0] * (len(num1) + len(num2)) # Allocating result
    num1, num2 = num1[::-1], num2[::-1]

    for i1 in range(len(num1)):
        for i2 in range(len(num2)):
            currentNumber = int(num1[i1]) * int(num2[i2]) # Finding the actual product of two digits
            
            result[i1 + i2] += currentNumber # 81
            result[i1 + i2 + 1] += (result[i1 + i2] // 10) # adding 8 to the next idx
            result[i1 + i2] = result[i1 + i2] % 10 # Purring 1(single digit number) on that idx
    
    # Finding how many leading Os we have
    result, beginningIdx = result[::-1], 0
    while beginningIdx < len(result) and result[beginningIdx] == 0:
        beginningIdx += 1
    
    result = map(str, result[beginningIdx:]) # Converting ints into individual strings
    return "".join(result) # Joining all the individual string characters into a single string


# Slightly improved readable code
# O(n * m) time | O(n + m) space
def multiply(num1, num2):
    if "0" in [num1, num2]:
        return "0"
    
    result = [0] * (len(num1) + len(num2)) # Allocating result
    num1, num2 = num1[::-1], num2[::-1]

    for i1 in range(len(num1)):
        for i2 in range(len(num2)):
            currentNumber = int(num1[i1]) * int(num2[i2]) # Finding the actual product of two digits
            currentIdx = i1 + i2

            result[currentIdx] += currentNumber # 81
            result[currentIdx + 1] += (result[currentIdx] // 10) # adding 8 to the next idx
            result[currentIdx] = result[currentIdx] % 10 # Purring 1(single digit number) on that idx
    
    # Finding how many leading Os we have
    result, beginningIdx = result[::-1], 0
    while beginningIdx < len(result) and result[beginningIdx] == 0:
        beginningIdx += 1
    
    result = map(str, result[beginningIdx:]) # Converting ints into individual strings
    return "".join(result) # Joining all the individual string characters into a single string


# O(n) time | O(1) space
def canReachEnd(A):
    furthestReachSoFar, lastIdx = 0, len(A) - 1
    i = 0
    
    # Will stop if i > furthestReachSoFar: Because we reached an idx that we couldn't reach by following the rules.
    # Or furthestReachSoFar is already the lastIdx
    while i <= furthestReachSoFar and furthestReachSoFar < lastIdx:
        furthestReachSoFar = max(furthestReachSoFar, A[i] + i)
        i += 1

    return furthestReachSoFar >= lastIdx

