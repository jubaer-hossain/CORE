'''
- Mainly used to solve connectivity problem
- Required an extra auxiliary data structure: Array
- Initialize the array with the independent indices
'''

'''
Implementation of QuickFind. 

Time Complexity:
O(1) time for find() and connected() and O(N) for union() function

Space Complexity:
O(N) since we need to store the array of size N
'''
class UnionFind:
    def __init__(self, size): # Constractor
        self.root = [i for i in range(size)]

    def find(self, x): # O(1)
        return self.root[x]

    def union(self, x, y) -> None: # O(N), Because we need to travarse the entire array
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX
    
    def connected(self, x, y) -> bool: # O(1)
        return self.find(x) == self.find(y)

# Test Case
uf = UnionFind(10)

# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)

uf.union(3, 8)
uf.union(8, 9)

print(uf.connected(1, 5)) # True
print(uf.connected(3, 8)) # True
print(uf.connected(4, 9)) # False

uf.union(4, 9) # The set will become this: 1-2-5-6-7 3-8-9-4
print(uf.connected(4, 9)) # True


'''
Implementation of QuickUnion. 

Time Complexity:
O(N) time for find() and connected() and <= O(N) for union() function

Space Complexity:
O(N) since we need to store the array of size N
'''
class QuickUnion:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)

'''
For QuickFind the complexity is O(N) * O(N) which is DEFINITELY O(N^2)
For QuickUnion the complexity is <=O(N) for QuickUnion and O(N) for QuickFind. 
Which means it has "<=" Less than or equal to O(N^2) which is slightly efficient than QuickFind.
Because on QuickFind the complexity is DEFINITELY O(N^2) in every Union operation.

Space complexity is same O(N) for all of them
'''