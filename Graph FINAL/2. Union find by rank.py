class UnionFind:
    def __init__(self, size): # O(N) Space Time
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x): # O(logN) Time
        while x != self.root[x]:
            x = self.root[x]
        return x

    def unionByRank(self, x, y): # O(logN) Time
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y): # O(logN) Time
        return self.find(x) == self.find(y)


import unittest
class UnionFindTest(unittest.TestCase):
    def test_1(self):
        pass

    def test_2(self):
        ...

if __name__ == "__main__":
    uf = UnionFind(10)

    uf.unionByRank(1, 2)
    uf.unionByRank(2, 5)
    uf.unionByRank(5, 6)
    uf.unionByRank(6, 7)
    uf.unionByRank(3, 8)
    uf.unionByRank(8, 9)

    print(uf.connected(1, 5))
    print(uf.connected(5, 7))
    print(uf.connected(4, 9))

    uf.unionByRank(4, 9)

    print(uf.connected(4, 9))
    unittest.main()