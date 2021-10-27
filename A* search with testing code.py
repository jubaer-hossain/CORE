class Node:
    def __init__(self, row, col, value):
        self.id = str(row) + "-" + str(col)
        self.row = row
        self.col = col
        self.value = value
        self.distanceFromStart = float("inf") # G value
        self.estimatedDistanceToEnd = float("inf") # H = G + F
        self.cameFrom = None

def aStarAlgorithm(startRow, startCol, endRow, endCol, graph):
    nodes = initializeNodes(graph) # Converting 2D int array into 2D Node object array

    startNode = nodes[startRow][startCol]
    endNode = nodes[endRow][endCol]
    
    # print(startNode.value, startNode.id)
    startNode.distanceFromStart = 0
    startNode.estimatedDistanceToEnd = calculateManhattanDistance(startNode, endNode)


    print("Type of startNode:", type(startNode)) 
    print(startNode)

    print("Type of [startNode]:", type([startNode]))
    print([startNode])
    print(type(startNode) == type([startNode]))
    """
    Mainly here we are passing a list that contains only the start node.
    That's why using [startNode] cause that will convert it to a list. 
    If we pass MinHeap(startNode) then we are passing an object to the Heap.
    But a heap uses an array so that it's efficient to keep track of the top element 
    """

    nodesToVisit = MinHeap([startNode]) 
    

    while not nodesToVisit.isEmpty():
        currentMinDistanceNode = nodesToVisit.remove()

        if currentMinDistanceNode == endNode: # Break if we already reached the end node
            break
    
        neighbors = getNeighboringNodes(currentMinDistanceNode, nodes)
        for neighbor in neighbors:
            if neighbor.value == 1: # Obstacle
                continue

            tentativeDistanceToNeighbor = currentMinDistanceNode.distanceFromStart + 1 # checking if G score of each neighbor is lower
            if tentativeDistanceToNeighbor >= neighbor.distanceFromStart:
                continue
            
            # Updating G, H score and came from node of all acceptable neighbors
            neighbor.cameFrom = currentMinDistanceNode
            neighbor.distanceFromStart = tentativeDistanceToNeighbor
            neighbor.estimatedDistanceToEnd = tentativeDistanceToNeighbor + calculateManhattanDistance(neighbor, endNode)

            if not nodesToVisit.containsNode(neighbor):
                nodesToVisit.insert(neighbor)
            else:
                nodesToVisit.update(neighbor)
    
    return reconstructPath(endNode)


def initializeNodes(graph):
    nodes = []

    for i, row in enumerate(graph): # first row = [0, 0, 0, 0, 0]
        nodes.append([])
        for j, value in enumerate(row):
            nodes[i].append(Node(i, j, value)) # Creating a Node object with id, row, col, value, G, H and came from
    
    # TESTING: Printing each nodes with row and column index
    for i, row in enumerate(nodes):
        print("Row number: ", i)
        for j, value in enumerate(row):
            print(i, j, nodes[i][j], nodes[i][j].id, nodes[i][j].value)
        print()
    return nodes # Returns a 2D array of Node object. Imagine each node is a square block that holds all info about that block

def getNeighboringNodes(node, nodes):
    neighbors = []

    numRows = len(nodes)
    numCols = len(nodes[0])

    row = node.row
    col = node.col

    if row < numRows - 1: # Down
        neighbors.append(nodes[row + 1][col])
    if row > 0: # Up
        neighbors.append(nodes[row - 1][col])
    if col < numCols - 1: # Right
        neighbors.append(nodes[row][col + 1])
    if col > 0: # Left
        neighbors.append(nodes[row][col - 1])
    
    return neighbors

def calculateManhattanDistance(currentNode, endNode):
    currentRow = currentNode.row
    currentCol = currentNode.col
    endRow = endNode.row
    endCol = endNode.col

    return abs(currentRow - endRow) + abs(currentCol - endCol)

def reconstructPath(endNode):
    if not endNode.cameFrom:
        return []

    currentNode = endNode
    path = []

    while currentNode is not None:
        path.append([currentNode.row, currentNode.col])
        currentNode = currentNode.cameFrom

    return reversed(path)


class MinHeap:
    def __init__(self, array):
        self.nodePositionsInHeap = {node.id: idx for idx, node in enumerate(array)} # DON'T UNDERSTAND: What exactly are we storing in this map?
        self.heap = self.buildHeap(array)
        # print(nodePositionsInHeap)


    def isEmpty(self):
        return len(self.heap)

    # O(N) Time | O(1) Space
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)): # DON'T UNDERSTAND: Why using firstParentIdx + 1?
            self.siftDown(currentIdx, len(array) - 1, array)
        return array
    
    # O(log(N)) Time | O(1) Space
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 1 if currentIdx * 2 + 1 <= endIdx else -1
            if (childTwoIdx != -1 and heap[childTwoIdx].estimatedDistanceToEnd < heap[childOneIdx].estimatedDistanceToEnd):
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx

            if heap[idxToSwap].estimatedDistanceToEnd < heap[currentIdx].estimatedDistanceToEnd:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return
    
    # O(log(N)) Time | O(1) Space
    def siftUp(self, currnetIdx, heap):
        parentIdx = (currnetIdx - 1) // 2
        while currnetIdx > 0 and heap[currnetIdx].estimatedDistanceToEnd < heap[parentIdx].estimatedDistanceToEnd:
            self.swap(currnetIdx, parentIdx, heap)
            currnetIdx = parentIdx
            parentIdx = (currnetIdx - 1) // 2
    """
    If you look at this code from a birds eye view, it seems complicated. But it's actually not. 
    First you have to understand the concept REALLY REALLY WELL. Then when writing the code, 
    at a given momenet, you only focus on that small piece of logic on that line and move forward. 
    That will eventually create these massive complex Data Structures
    """

    # O(log(N)) Time | O(1) Space
    def remove(self):
        if self.isEmpty():
            return

        self.swap(0, len(self.heap) - 1, self.heap)
        node = self.heap.pop() # Popping the top node from the heap
        del self.nodePositionsInHeap[node.id] # Deleting that node from our map
        self.siftDown(0, len(self.heap) - 1, self.heap) # Sifting down the new first element so that it get placed at it's respected position
        return node

    # O(log(N)) Time | O(1) Space
    def insert(self, node):
        self.heap.append(node)
        self.nodePositionsInHeap[node.id] = len(self.heap) - 1 # Adding on the map with key as node id and value as it's index position on the heap
        self.siftUp(len(self.heap) - 1, self.heap)
        
    def swap(self, i, j, heap):
        # Swapping the indexes/ids of nodes in heap
        self.nodePositionsInHeap[heap[i].id] = j
        self.nodePositionsInHeap[heap[j].id] = i
        
        # Swapping the two nodes' position in array
        heap[i], heap[j] = heap[j], heap[i]

    def containsNode(self, node):
        return node.id in self.nodePositionsInHeap # We use the map to quickly find out if a node already exist in the heap somewhere

    def update(self, node):
        self.siftUp(self.nodePositionsInHeap[node.id], self.heap)
        """
        Mainly suppose heap[6] position e ekta node ase jeita amra update korte cacchi with new value.
        So ei value ta quickly paoar upay hocche map theke nodePositionsInHeap[node.id] dilei map e bole dibe oitar
        current position heap er kothay.
        Then amra heap array te oitar current position and full heap array ta siftUp er moddhe pass korbo jate oi node er new value ta
        heap e update hoy and node ta correct position e jaite pare
        
        Also every siftUp or siftDown er moddhei swap() method e amra map er moddheo oi node er index update kori je heap er kon
        index e oita jacche
        """
    


        

# TESTING:
graph = [
  [0, 0, 0, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 0, 0, 0],
  [1, 0, 1, 1, 1],
  [0, 0, 0, 0, 0]
]

print(aStarAlgorithm(0, 1, 4, 3, graph))
# initializeNodes(graph)
# print(initializeNodes(graph))
# print(type(initializeNodes(graph)[0][0]))