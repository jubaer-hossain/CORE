# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



def findNodesDistanceK(tree, target, k):
    nodeValuesToParentObject = {}

    getNodesToParents(tree, nodeValuesToParentObject)

    targetNode = getTargetNode(tree, target, nodeValuesToParentObject)

    # (nodeObject, distanceFromTarget)
    queue = [(targetNode, 0)]
    seen = {targetNode.value}

    while len(queue) > 0:
        nodeInfo = queue.pop(0)

        currentNode, distanceFromTarget = nodeInfo

        if distanceFromTarget == k:
            result = []

            for i in range(len(queue)):
                remainingNodes = queue.pop()
                node, distance = remainingNodes
                result.append(node.value)
            result.append(currentNode.value)

            return result

        # Need to add connected nodes
        connectedNodes = [currentNode.left, currentNode.right, nodeValuesToParentObject[currentNode.value]]

        for node in connectedNodes:
            if node is None:
                continue

            if node.value in seen:
                continue
            
            seen.add(node.value)
            queue.append((node, distanceFromTarget + 1))

    return []
    
        
        

def getTargetNode(node, targetValue, nodeValuesToParentObject):
    if node.value == targetValue:
        return node
    parentNode = nodeValuesToParentObject[targetValue]

    if parentNode.left is not None and parentNode.left.value == targetValue:
        return parentNode.left
    
    return parentNode.right

def getNodesToParents(node, nodeValuesToParentObject, parent = None):
    if node is not None:
        nodeValuesToParentObject[node.value] = parent
        getNodesToParents(node.left, nodeValuesToParentObject, node)
        getNodesToParents(node.right, nodeValuesToParentObject, node)