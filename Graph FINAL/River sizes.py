# O(wh) time | O(wh) space
def riverSizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])): # Safe to run until i just in case it's an uneven matrix

            if visited[i][j]:
                continue

            traverseNode(i, j, matrix, visited, sizes) # DFS

    return sizes

# DFS
def traverseNode(i, j, matrix, visited, sizes):
    currentRiverSize = 0

    # 1. Create a stack to keep track of all nodes
    nodesToExplore = [[i, j]]

    while len(nodesToExplore):
        # 2. Pop the topmost node from the stack
        currentNode = nodesToExplore.pop()

        # 3. Uncouple and get idx i and j
        i = currentNode[0]
        j = currentNode[1]

        # 4. We don't need to run DFS on visited nodes
        if visited[i][j]:
            continue

        # 5. If we come here that means the currentNode has not visited before so we mark it as VISITED
        visited[i][j] = True

        # 6. Also if the currentNode is a land then we don't need to run DFS from it
        if matrix[i][j] == 0:
            continue

        # 7. Increase currentRiverSize
        currentRiverSize += 1

        # 8. Get all neighbor nodes. unvisitedNeighbors = [[1,0], [1,1], [2,1]] etc
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)

        # 9. Adding all connected unvisited nodes in the stack
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)

    # 10. Finally if the riverSize is greater than 0 then we append it to final result
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)


def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []

    # Up
    if i > 0 and not visited[i - 1][j]:
        unvisitedNeighbors.append([i - 1, j])

    # Down
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisitedNeighbors.append([i + 1, j])

    # Left
    if j > 0 and not visited[i][j - 1]:
        unvisitedNeighbors.append([i, j - 1])

    # Right
    if j < len(matrix[i]) - 1 and not visited[i][j + 1]:
        unvisitedNeighbors.append([i, j + 1])

    return unvisitedNeighbors



