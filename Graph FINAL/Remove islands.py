# O(wh) time | O(wh) space
def removeIslands(matrix):
    onesConnectedToBorder = [[False for col in matrix[0]] for row in matrix] # For all columns in a row and for all rows in the matrix

    # 1. Find all nodes that are not islands
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):

            # 2. Finding if the currentNode is at border
            rowIsBorder = row == 0 or row == len(matrix) - 1
            colIsBorder = col == 0 or col == len(matrix[row]) - 1

            isBorder = rowIsBorder or colIsBorder

            if not isBorder:
                continue

            if matrix[row][col] != 1: # Not part of any island
                continue

            # 3. Run DFS from the currentNode to find all connected 1s
            findOnesConnectedToBorder(row, col, matrix, onesConnectedToBorder)

    # 4. Remove 1 values that are not connected to border
    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[row]) - 1):

            # 5. If they are connected to border then we don't need to change the value
            if onesConnectedToBorder[row][col]:
                continue

            # 6. Other change the value to 0
            matrix[row][col] = 0

    return matrix

def findOnesConnectedToBorder(row, col, matrix, onesConnectedToBorder):
    stack = [(row, col)]

    while len(stack) > 0:
        currentNode = stack.pop()

        currentRow, currentCol = currentNode

        # 1. Already visited
        if onesConnectedToBorder[currentRow][currentCol] is True:
            continue

        onesConnectedToBorder[currentRow][currentCol] = True

        # 2. Note that here we are getting all the neighbors. This does not handle one case. We should check and only get unvisited neighbors instead of just neighbors
        neighbors = getNeighbors(currentRow, currentCol, matrix)

        # 3. Append all the neighbors 
        for neighbor in neighbors:
            row, col = neighbor

            # 4. Checking if the neighbor node is 1(part of connected land) or not
            if matrix[row][col] != 1:
                continue

            stack.append(neighbor)

def getNeighbors(row, col, matrix):
    neighbors = []

    # Be careful here cause array's are indxed from 0. So totaRow's should be len(matrix) - 1
    totalRows = len(matrix)
    totalCols = len(matrix[row])

    if row > 0:
        neighbors.append((row - 1, col))
    if row + 1 < totalRows:
        neighbors.append((row + 1, col))

    if col > 0:
        neighbors.append((row, col - 1))
    if col + 1 < totalCols:
        neighbors.append((row, col + 1))

    return neighbors
            



            