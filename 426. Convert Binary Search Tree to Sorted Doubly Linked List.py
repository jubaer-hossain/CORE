"""
1 - 2 - 3 - 4 - 5
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        leftMost, rightMost = self.connectNodes(root)
        self.connectTwoNodes(rightMost, leftMost)
        return leftMost

    def connectNodes(self, node):
        if node.left is None:
            leftMost = node
        else:
            leftSubtreeLeftmost, leftSubtreeRightmost = self.connectNodes(node.left)
            self.connectTwoNodes(leftSubtreeRightmost, node)
            leftMost = leftSubtreeLeftmost

        if node.right is None:
            rightMost = node
        else:
            rightSubtreeLeftmost, rightSubtreeRightmost = self.connectNodes(node.right)
            self.connectTwoNodes(node, rightSubtreeLeftmost)
            rightMost = rightSubtreeRightmost

        return (leftMost, rightMost)
    
    def connectTwoNodes(self, leftNode, rightNode):
        leftNode.right = rightNode
        rightNode.left = leftNode



class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """


        def connectNodes(node):
            if node.left is None:
                leftMost = node
            else:
                leftSubtreeLeftmost, leftSubtreeRightmost = connectNodes(node.left)
                connectTwoNodes(leftSubtreeRightmost, node)
                leftMost = leftSubtreeLeftmost

            if node.right is None:
                rightMost = node
            else:
                rightSubtreeLeftmost, rightSubtreeRightmost =connectNodes(node.right)
                connectTwoNodes(node, rightSubtreeLeftmost)
                rightMost = rightSubtreeRightmost

            return (leftMost, rightMost)
        
        def connectTwoNodes( leftNode, rightNode):
            leftNode.right = rightNode
            rightNode.left = leftNode
        
        leftMost, rightMost = connectNodes(root)
        rightMost.right = leftMost
        leftMost.left = rightMost
        return leftMost


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        leftMost, rightMost = self.connectNodes(root)
        self.connectTwoNodes(rightMost, leftMost)
        return leftMost

    def connectNodes(self, node):
        if node.left is None and node.right is None:
            return (node, node)
            
        if node.left is None:
            leftMost = node
        else:
            leftSubtreeLeftmost, leftSubtreeRightmost = self.connectNodes(node.left)
            self.connectTwoNodes(leftSubtreeRightmost, node)
            leftMost = leftSubtreeLeftmost

        if node.right is None:
            rightMost = node
        else:
            rightSubtreeLeftmost, rightSubtreeRightmost = self.connectNodes(node.right)
            self.connectTwoNodes(node, rightSubtreeLeftmost)
            rightMost = rightSubtreeRightmost

        return (leftMost, rightMost)
    
    def connectTwoNodes(self, leftNode, rightNode):
        leftNode.right = rightNode
        rightNode.left = leftNode