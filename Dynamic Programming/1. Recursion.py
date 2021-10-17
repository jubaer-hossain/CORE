'''Recursive solution of all path from top to bottom of a matrix
Given a N x M matrix. Find the number of ways/paths you can go from the top left to the bottom right corner. N = M <= 100

Test cases:
Input:
n = 1, m = 1

Output:
1
Cause ekta 1 x 1 Matrix e upor theke niche jaoar path ektai

Input:
n = 5, m = 1

Output:
1
Cause ekta 5 x 1 matrix e upor theke niche jaoar path ektai

Input:
n = 2, m = 2

Output:
2
Cause ekta 2 x 2 matrix e top left theke bottom right e jaoar path 2 ta. 
Path-1: 0, 0 -> 1, 0 -> 1, 1
Path-2:  0, 0 -> 0, 1 -> 1, 1
'''
def allPaths(m, n):
    if n == 1 or m == 1:
        return 1
    return allPaths(m - 1, n) + allPaths(m, n - 1)

print(allPaths(3, 3))
print(allPaths(4, 3))
print(allPaths(3, 5))
print(allPaths(10, 10))
print(allPaths(3, 11))
print(allPaths(14, 16))
print(allPaths(19, 3))

'''
Write a function that counts the number of ways you can partition n objects using parts upto m (Assuming m >= 0)
'''
def count_partitions(n, m):
    if n == 0:
        return 1
    elif m == 0 or n <= 0:
        return 0
    else:
        return count_partitions(n - m, m) + count_partitions(n, m - 1)

print(count_partitions(9, 5))