'''Recursive solution of all path from top to bottom of a matrix'''
def allPaths(m, n):
    if n == 1 or m == 1:
        return 1
    return allPaths(m - 1, n) + allPaths(m, n - 1)

print(allPaths(3, 3))