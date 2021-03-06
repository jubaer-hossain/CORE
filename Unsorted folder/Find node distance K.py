def findNodesDistanceK(tree, target, k):
    nodesToParents = {} # Node "values" to parentNode "object"
    populateNodesToParents(tree, nodesToParents)

    targetNode = getNodeFromValue(tree, nodesToParents, target)

    return breathFirstSearchForNodesDistanceK(targetNode, nodesToParents, k)

def breathFirstSearchForNodesDistanceK(targetNode, nodesToParents, k):
    queue = [(targetNode, 0)] # FIFO 
    seen = {targetNode.value} # Set

    while len(queue) > 0:
        currentNode, distanceFromTarget = queue.pop(0) # FIFO order that's why popping the first element

        if distanceFromTarget == k:
            nodesDistanceK = [node.value for node, _ in queue] # Iterating over the array and only taking node.value and adding it to the result array
            nodesDistanceK.append(currentNode.value) # Also adding the final popped node
            return nodesDistanceK

        connectedNodes = [currentNode.left, currentNode.right, nodesToParents[currentNode.value]] 
        for node in connectedNodes:
            if node is None:
                continue
            if node.value in seen: # If we already processed that node before
                continue
            
            seen.add(node.value)
            queue.append((node, distanceFromTarget + 1))
    
    return []

def getNodeFromValue(tree, nodesToParents, value):
    if tree.value == value: # If the target node is at root
        return tree
    
    parentNode = nodesToParents[value] # Getting the node's parent
    if parentNode.left and parentNode.left.value == value: # Checking if the targetNode is parent's left or right child
        return parentNode.left
    return parentNode.right

# Mapping every Value to it's Parent
def populateNodesToParents(node, nodesToParents, parentNode = None):
    if node is not None:
        nodesToParents[node.value] = parentNode
        populateNodesToParents(node.left, nodesToParents, node)
        populateNodesToParents(node.right, nodesToParents, node)