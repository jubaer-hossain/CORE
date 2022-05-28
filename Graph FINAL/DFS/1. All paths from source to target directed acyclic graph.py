class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node):
            path.append(node)
            if node == len(graph) - 1:
                paths.append(path.copy())
                return

            next_nodes = graph[node]
            for next_node in next_nodes:
                dfs(next_node)
                path.pop()

        paths = [] # The result array 
        path = [] # A single path
        if not graph or len(graph) == 0: # If the graph is empty, it will return empty array
            return paths
        dfs(0)
        return paths


graph1 = [[4,3,1],[3,2,4],[3],[4],[]] # Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
graph2 = [[1,2,3],[2],[3],[]] # Output: [[0,1,2,3],[0,2,3],[0,3]]
graph3 = [[1,3],[2],[3],[]] # Output: [[0,1,2,3],[0,3]]