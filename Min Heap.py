class MinHeap:
    def __init__(self, array):
        self.heap = buildHeap(array)

    # O(N) Time | O(1) Space
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2 # Formula: floor((Last element index - 1)/ 2)
        for currentIdx in reversed(range(firstParentIdx)): # Mainly first parent theke ekdm top porjonto prottekta element ke individually dhore sift down korbe. And sift down e jehetu swap ache so prottekta parent element re sift down korle individually shob gula nij nij jayga moto boshe jabe Min Heap er properties moto
            self.siftDown(currentIdx, len(array) - 1, array)
        return array
    
    # O(logN) Time | O(1) Space
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx: # We will siftDown until we reach the last leaf of the tree
            childTwoIdx = currentIdx * 2 + 1 if currentIdx * 2 + 1 <= endIdx else -1
            
            # Selecting which child to swap with the current node
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            
            # If the smallest child is larger than the current node element
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return

    # O(logN) Time | O(1) Space
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    # O(1) Time | O(1) Space
    def peek(self):
        return self.heap[0]

    # O(logN) Time | O(1) Space
    def remove(self): # Basically returns and deletes the top/min element
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    # O(logN) Time | O(1) Space
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]