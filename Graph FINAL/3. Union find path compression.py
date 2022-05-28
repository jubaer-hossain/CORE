# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def print(self):
        print(self.root)

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Test Case
uf = UnionFind(12)
# 1-2-5-6-7 3-8-9 4
uf.print()
uf.union(0, 1)
uf.union(1, 2)
uf.union(2, 3)
uf.union(3, 4)
uf.print()
uf.union(5, 6)
uf.union(6, 7)
uf.union(7, 8)
uf.union(8, 9)
uf.print()

uf.union(4, 5)
uf.print()
print(uf.find(9))
uf.print()
uf.union(9, 10)
uf.print()