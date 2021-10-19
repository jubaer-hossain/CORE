'''
[
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

[
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
'''
class UnionFind:
    def __init__ (self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find_provinces(self):
        root_provinces = []
        for i in range(len(self.root)):
            if i not in root_provinces:
                root_provinces.append(i)
        return len(root_provinces) - 1


class Solition:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        cities = UnionFind(n + 1)

        for i in range(n + 1):
            for j in range(n + 1):
                cities.union(i, j)

        provinces = 0
