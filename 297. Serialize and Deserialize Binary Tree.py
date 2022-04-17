class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# O(n) time | O(n) space, cause we traverse and store the whole tree in both cases
class Codec:
    def serialize(self, root, string = ""):
        if root is None:
            string += 'None,'
        else: # Pre-order traversal serialisation
            string += str(root.val) + ','
            string = self.serialize(root.left, string)
            string = self.serialize(root.right, string)
        return string

    def deserialize(self, string):
        # So here this nodeList is turning a string of "2,3,4,None,None,5,None"
        # Into a list of [2, 3, 4, None, None, 5, None] excluding commas
        nodesList = string.split(",")
        return self.deserializeTree(nodesList)

    def deserializeTree(self, nodesList):
        # When we move past a leaf node it has to return None
        # Otherwise we will end up with infinite recursion
        if nodesList[0] == 'None': 
            nodesList.pop(0)
            return None
        
        root = TreeNode(nodesList[0])
        nodesList.pop(0)
        
        root.left = self.deserializeTree(nodesList)
        root.right = self.deserializeTree(nodesList)

        return root