class Solution:
    
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)
    
    
    def isMirror(self, t1, t2):
        if not t1 and not t2: return True
        if not t1 or not t2: return False
        return t1.val == t2.val and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)


class Solution:
    def isSymmetric(self, root):
        return self.isMirror(root, root)
    
    def isMirror(self, nodeOne, nodeTwo):
        if nodeOne is None and nodeTwo is None:
            return True
        if nodeOne is None or nodeTwo is None:
            return False
        
        leftIsMirror = self.isMirror(nodeOne.left, nodeTwo.right)
        rightIsMirror = self.isMirror(nodeOne.right, nodeTwo.left)

        return nodeOne.val == nodeTwo.val and leftIsMirror and rightIsMirror


# Level order traversal
from collections import deque

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = deque([root])
        while len(q) != 0:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val if node is not None else None)    
                if node is not None:
                    for child in (node.left, node.right):
                        q.append(child) 
            if level != level[::-1]:
                return False
        return True
        