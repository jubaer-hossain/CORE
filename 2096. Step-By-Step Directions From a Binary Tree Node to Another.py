# O(n) time | O(n) space
class Solution:
    def getDirections(self, root, startValue, destValue):
        startNodePathFromRoot, destNodePathFromRoot = [], []
        
        # startNodePathFromRoot =. Python passes array by reference. So do not assign it to Array. Array will modify itself
        self.findPath(root, startValue, startNodePathFromRoot)
        # destNodePathFromRoot = 
        self.findPath(root, destValue, destNodePathFromRoot)
        
        while len(startNodePathFromRoot) > 0 and len(destNodePathFromRoot) > 0 and startNodePathFromRoot[-1] == destNodePathFromRoot[-1]:
            startNodePathFromRoot.pop()
            destNodePathFromRoot.pop()
        
        return "".join("U" * len(startNodePathFromRoot)) + "".join(reversed(destNodePathFromRoot)) # Reversed cause recursive calls
        # return the path from the bottom up.

    # Finds path form the root to a targetValue node
    def findPath(self, node, targetValue, currentPath):
        if node.val == targetValue:
            return True # Base case
        
        if node.left is not None and self.findPath(node.left, targetValue, currentPath):
            currentPath += "L"
        elif node.right is not None and self.findPath(node.right, targetValue, currentPath):
            currentPath += "R"
        return currentPath # Every call returns and modifies the array at the same time
        # The final call modifies and returns the array. But that returning doesn't really matter,
        # because we are also modifying the string/array at the same time

"""
      10
     /   \
    5     15
   / \   /   \
  2   5 13   22
 /      / \
1      12 14

Build directions for both start and destination from the root.
    Say we get "LLRRL" and "LRR".
Remove common prefix path.
    We remove "L", and now start direction is "LRRL", and destination - "RR"
Replace all steps in the start direction to "U" and add destination direction.
    The result is "UUUU" + "RR".
"""


# Approach-2: Lowest common ancestor method
class Solution:
    # O(n) time | O(log(n)) space
    def getDirections(self, root, startValue, destValue):
        lowestCommonAncestor = self.getCommonAncestor(root, startValue, destValue)
        
        stack = [(lowestCommonAncestor, "")]
        
        startPath = destPath = ""
        while len(stack) > 0:
            node, path = stack.pop()
            if node.val == startValue:
                startPath = path
            if node.val == destValue:
                destPath = path
            
            if node.left is not None:
                stack.append((node.left, path + "L")) # We add the current direction "L" or "R" with the existing path of that node
            if node.right is not None:    
                stack.append((node.right, path + "R"))
        
        return "U"*len(startPath) + destPath


    # O(n) time | O(log(n)) space
    def getCommonAncestor(self, node, startValue, destValue):
        if node is None:
            return False
        
        nodePresentInLeftSubtree = self.getCommonAncestor(node.left, startValue, destValue)
        nodePresentInRightSubree = self.getCommonAncestor(node.right, startValue, destValue)

        if (nodePresentInLeftSubtree and nodePresentInRightSubree) or (node.val in [startValue, destValue]):
            return node
        else:
            return nodePresentInLeftSubtree or nodePresentInRightSubree


