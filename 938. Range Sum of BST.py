# O(n) time | O(n) space
class Solution(object):
    def rangeSumBST(self, root, low, high):
        inOrderTraversal = []
        inOrderTraversal = self.getInOrderTraversal(root, inOrderTraversal)
        result = 0
        for i in range(0, len(inOrderTraversal)):
            if inOrderTraversal[i] >= low and inOrderTraversal[i] <= high:
                result += inOrderTraversal[i]
        return result


    def getInOrderTraversal(self, node, array):
        if node is not None:
            self.getInOrderTraversal(node.left, array)
            array.append(node.val)
            self.getInOrderTraversal(node.right, array)
        return array


# O(n) time | O(h) space
class Solution(object):
    def rangeSumBST(self, root, low, high):
        if root is None:
            return 0
        
        leftSubtreeSum = self.rangeSumBST(root.left, low, high)
        rightSubtreeSum = self.rangeSumBST(root.right, low, high)

        currentNodeSum = leftSubtreeSum + rightSubtreeSum

        if root.val >= low and root.val <= high:
            currentNodeSum += root.val
        
        return currentNodeSum

