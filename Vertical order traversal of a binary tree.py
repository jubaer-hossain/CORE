import collections


class Solution:
    def verticalTraversal(self, root):
        nodeList = []
        self.populateNodeRowColumn(root, 0, 0, nodeList)
        
        nodeList.sort() # This is basically a 3D sort. So smallest column comes first, then smallest row, then smallest value

        result = []
        currentColumnIdx = nodeList[0][0] # From 0th Row, 0th Idx which is the lowest column
        currentColumn = []

        for column, row, value in nodeList:
            if column == currentColumnIdx:
                currentColumn.append(value)
            else: # End of binary tree vertical column
                result.append(currentColumn)
                currentColumnIdx = column
                currentColumn = [value] # Deleting all previous values and only putting the next Column's value that we just got
        
        # Add the last column becuase when we looped out of the for loop we still haven't added the last currentBinaryTreeColumn's values
        result.append(currentColumn)
        return result


    def populateNodeRowColumn(self, node, column, row, nodeList):
        if node is not None:
            nodeList.append((column, row, node.val))
            self.populateNodeRowColumn(node.left, column - 1, row + 1, nodeList)
            self.populateNodeRowColumn(node.right, column + 1, row + 1, nodeList)

# Approach 2: DFS with partition sorting
class Solution:
    def verticalTraversal(self, root):
        columnTable = collections.defaultdict(list)
        minColumn, maxColumn = self.populateColumnTable(root, 0, 0, columnTable)
        
        result = []
        for col in range(minColumn, maxColumn + 1): # Because if we have 5 column then default python range() will iterate until 4. To include 5 we need to iterate from minCol to maxCol + 1
            result.append([val for row, val in sorted(columnTable[col])])
        return result

    def populateColumnTable(self, node, row, column, columnTable, minCol = 0, maxCol = 0):
        if node is not None:
            columnTable[column].append((row, node.val))

            leftCol, _ = self.populateColumnTable(node.left, row + 1, column - 1, columnTable, minCol, maxCol)
            _, rightCol = self.populateColumnTable(node.right, row + 1, column + 1, columnTable, minCol, maxCol)
            minCol = min(column, leftCol)
            maxCol = max(column, rightCol)
            return minCol, maxCol