# O(n) time | O(n) space
def lowestCommonAncestor(self, root, p, q):
    return self.findCommonAncestor(root, p, q)

def findCommonAncestor(self, node, p, q):
    if node is None:
        return False # Base case: None node should return False

    nodePresentInLeftSubtree = self.findCommonAncestor(node.left, p, q)
    nodePresentInRightSubtree = self.findCommonAncestor(node.right, p, q)

    # nodePresentInLeftSubtree and nodePresentInRightSubtree -> Means we found a node that's left and right child are "p" and "q"
    # node in [p, q] -> Means current node is one of p or q so we need to pass that upward
    if (nodePresentInLeftSubtree and nodePresentInRightSubtree) or node in [p, q]:
        return node
    else:
        return nodePresentInLeftSubtree or nodePresentInRightSubtree


# Iterative approach
# O(n) time | O(n) space
def lowestCommonAncestor(self, root, p, q):
    stack = [root]

    nodeToParent = {root : None}

    # Storing each node to it's parent until we store both p and q's parent
    while p not in nodeToParent or q not in nodeToParent:
        node = stack.pop()

        if node.left is not None:
            nodeToParent[node.left] = node
            stack.append(node.left)
        if node.right is not None:
            nodeToParent[node.right] = node
            stack.append(node.right)

    ancestors = set()

    # From the node p, we are traversing upword on the parent tree and storing each value
    # So basically we are storing all the parents/ancestors of the node p
    while p is not None:
        ancestors.add(p)
        p = nodeToParent[p]

    # Again starting from q we traverse upword and store all the parents/ancestors
    # But this time we stop when we find that one parent is already in the set. Because that means that parent is the common ancestor for p and q since we are traversing from the bottom
    while q not in ancestors:
        ancestors.add(q)
        q = nodeToParent[q]

    return q # We return q because since we traversed upword and overwrite q's value, the current q is actually the common ancestor node for both p and q

# For a BST
# O(logN) time since we are traversing 1 node in each BST level | O(1) space
def lowestCommonAncestor(self, root, p, q):
    currentNode = root

    while currentNode:
        if p.val < currentNode.val and q.val < currentNode.val:
            currentNode = currentNode.left
        elif p.val > currentNode.val and q.val > currentNode.val:
            currentNode = currentNode.right
        else: # Either this node is one of p or q, or this is the split point
            return currentNode # Returning since we are gurrenteed to have a solution



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
            # We force them to change direction at the root node to Neutralize the gap to reach the root so that in the next iteration they can meet at a common node
            p1 = p1.parent if p1.parent is not None else q
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
        
        leftSubtreeDeepestNodeDepth, leftSubtreeLca = self.getCommonAncestor(node.left)
        rightSubtreeDeepestNodeDepth, rightSubtreeLca = self.getCommonAncestor(node.right)

        if leftSubtreeDeepestNodeDepth > rightSubtreeDeepestNodeDepth:
            return (leftSubtreeDeepestNodeDepth + 1, leftSubtreeLca)
        elif rightSubtreeDeepestNodeDepth > leftSubtreeDeepestNodeDepth:
            return (rightSubtreeDeepestNodeDepth + 1, rightSubtreeLca)
        else:
            return (leftSubtreeDeepestNodeDepth + 1, node) # Note that we are returning currentNode here
        