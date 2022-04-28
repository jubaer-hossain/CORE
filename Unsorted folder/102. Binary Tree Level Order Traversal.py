# Recursive DFS because first we finish the whole left subtree and then go to right
# O(n) time | O(n) space including the output array. O(h) space for a balanced tree
class Solution(object):
    def levelOrder(self, root):
        levelOrderTraversal = []
        levelOrderTraversal = self.getLevelOrderTraversal(root, 0, levelOrderTraversal)
        return  levelOrderTraversal
    
    def getLevelOrderTraversal(self, node, currentLevel, levelOrderTraversal):
        if node is not None:
            if len(levelOrderTraversal) == currentLevel:
                levelOrderTraversal.append([])
            
            levelOrderTraversal[currentLevel].append(node.val)

            self.getLevelOrderTraversal(node.left, currentLevel + 1, levelOrderTraversal)
            self.getLevelOrderTraversal(node.right, currentLevel + 1, levelOrderTraversal)
        
        return levelOrderTraversal


# BFS / iterative implementation with deque
# O(n) time | O(n) space including the output array. O((n + 1) / 2) space for a balanced tree
# cause on a balanced binary tree of n nodes we have (n + 1) / 2 leaf nodes
from collections import deque
from http.cookies import Morsel
from json import tool
class Solution(object):
    def levelOrder(self, root):
        levelOrderTraversal = []
        if root is None: # If we are given an empty tree
            return levelOrderTraversal
        
        currentLevel = 0
        queue = deque([root])

        while len(queue) > 0:
            levelOrderTraversal.append([])
            
            totalElementsInCurrentLevel = len(queue)

            for i in range(totalElementsInCurrentLevel):
                node = queue.popleft() # FIFO
                levelOrderTraversal[currentLevel].append(node.val)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            currentLevel += 1
        
        return levelOrderTraversal

# Bottom up level order traversal: We can return levelOrderTraversal[::-1] as shortcut

# Traversing from the bottom up technique
class Solution:
    def levelOrderBottom(self, root):
        treeHeight = self.getTreeHeight(root)
        levelOrderTraversalBottomUp = [[] for i in range(treeHeight)]

        levelOrderTraversalBottomUp = self.getLevelOrderBottomUp(root, levelOrderTraversalBottomUp, treeHeight - 1)
    
    def getTreeHeight(self, node):
        if node is None:
            return 0
        return 1 + max(self.getTreeHeight(node.left), self.getTreeHeight(node.right))
    
    def getLevelOrderBottomUp(self, node, levelOrderTraversalBottomUp, treeHeight):
        if treeHeight >= 0 and node is not None:
            self.getLevelOrderBottomUp(node.left, levelOrderTraversalBottomUp, treeHeight - 1)
            self.getLevelOrderBottomUp(node.right, levelOrderTraversalBottomUp, treeHeight - 1)
            levelOrderTraversalBottomUp[treeHeight].append(node.val)

