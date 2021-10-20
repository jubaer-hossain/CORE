from typing import List


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    def dfs(node):
        path.append(node)
        if node == len(graph) - 1:
            paths.append(path.copy())
            return

        next_nodes = graph[node]
        for next_node in next_nodes:
            dfs(next_node)
            path.pop()

    paths = []
    path = []
    if not graph or len(graph) == 0:
        return paths
    dfs(0)
    return paths

arr = [[1, 2], [3], [3], []]
# arr = [[1, 2, 4], [3], [3], [4], [1, 2, 3]]
print(allPathsSourceTarget(arr))