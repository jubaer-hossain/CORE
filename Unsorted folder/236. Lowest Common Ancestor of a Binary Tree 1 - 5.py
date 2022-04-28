# O(n) time | O(n) space
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        return self.getCommonAncestor(root, p, q)
    
    def getCommonAncestor(self, node, p, q):
        if node is None:
            return None # Base case: None node should return False
        
        nodePresentInLeftSubtree = self.getCommonAncestor(node.left, p, q)
        nodePresentInRightSubtree = self.getCommonAncestor(node.right, p, q)

        if (nodePresentInLeftSubtree and nodePresentInRightSubtree) or (node in [p, q]):
            return node
        else:
            return nodePresentInLeftSubtree or nodePresentInRightSubtree


# LCA-2: where either p or q is not present in the tree
# O(n) time | O(n) space
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        result = self.getCommonAncestor(root, p, q)

        if result is None: # No node is present
            return result
        else:
            if (result == p and self.getCommonAncestor(result, q, q) == None) or (result == q and self.getCommonAncestor(result, p, p) == None):
                # One node is present but other node is missing
                return None
            else: # Both nodes present and result is their lowest common ancestor
                return result

    
    def getCommonAncestor(self, node, p, q):
        if node is None:
            return None # Base case: None node should return False
        
        nodePresentInLeftSubtree = self.getCommonAncestor(node.left, p, q)
        nodePresentInRightSubtree = self.getCommonAncestor(node.right, p, q)

        if (nodePresentInLeftSubtree and nodePresentInRightSubtree) or (node in [p, q]):
            return node
        else:
            return nodePresentInLeftSubtree or nodePresentInRightSubtree

# LCA-3: We have reference to the parent node. 
# O(n) time | O(1) space
class Solution(object):
    def lowestCommonAncestor(self, p, q):
        p1 = p
        p2 = q
        
        while p1 != p2:
            p1 = p1.parent if p1.parent is not None else q # We force them to change direction at the root node
            p2 = p2.parent if p2.parent is not None else p
        
        return p1

# LCA-4: with a list of nodes
# O(n^2) time cause the nodes are not sorted. We can reduce it by sorting the nodes | O(h) space
class Solution:
    def lowestCommonAncestor(self, root, nodes):
        return self.getCommonAncestor(root, nodes)
    
    def getCommonAncestor(self, node, nodes):
        if node is None:
            return None # Base case: None node should return False
        
        nodePresentInLeftSubtree = self.getCommonAncestor(node.left, nodes)
        nodePresentInRightSubtree = self.getCommonAncestor(node.right, nodes)

        if (nodePresentInLeftSubtree and nodePresentInRightSubtree) or (node in nodes):
            return node
        else:
            return nodePresentInLeftSubtree or nodePresentInRightSubtree


# LCA Deepest leaves
# Very trivial approach. Find left info and find right info. Compare and add +1 to the height and bubble up the info
# O(n) time | O(h) space
class Solution:
    def lcaDeepestLeaves(self, root):
        deepestNodeDepth, deepestNodeLca = self.getLca(root)
        return deepestNodeLca
    
    def getLca(self, node):
        if node is None:
            return (0, None)
        
        leftSubtreeHeight, leftSubtreeLca = self.getLca(node.left)
        rightSubtreeHeight, rightSubtreeLca = self.getLca(node.right)

        if leftSubtreeHeight > rightSubtreeHeight:
            return leftSubtreeHeight + 1, leftSubtreeLca
        elif leftSubtreeHeight < rightSubtreeHeight:
            return rightSubtreeHeight + 1, rightSubtreeLca
        else:
            return leftSubtreeHeight + 1, node


class Solution:
    def lcaDeepestLeaves(self, root):
        deepestNodeDepth, deepestNodeLca = self.getCommonAncestor(root)
        return deepestNodeLca
    
    def getCommonAncestor(self, node):
        if node is None:
            return (0, None)
        
        leftSubtreeDeepestNode, leftSubtreeLca = self.getCommonAncestor(node.left)
        rightSubtreeDeepestNode, rightSubtreeLca = self.getCommonAncestor(node.right)

        if leftSubtreeDeepestNode > rightSubtreeDeepestNode:
            return (leftSubtreeDeepestNode + 1, leftSubtreeLca)
        elif rightSubtreeDeepestNode > leftSubtreeDeepestNode:
            return (rightSubtreeDeepestNode + 1, rightSubtreeLca)
        else:
            return (leftSubtreeDeepestNode + 1, node)
        