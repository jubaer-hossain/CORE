# O(n^2) time | O(n) space for slicing
def buildTree(self, preorder, inorder):
    # 0. Base case: If any array(sliced array) is empthy then return None
    if not preorder or not inorder:
        return None

    # 1. Create root node of the current Subtree
    root = TreeNode(preorder[0])

    # 2. Find that node's idx from the inOrder array. It's gonna be the middle node
    mid = inorder.index(preorder[0]) 
    # Here mid = number of leftNodes in the inOrder traversal and number of leftNodes that are there AFTER the rootIdx/firstIdx in the preOrder traversal. So if mid = 1 that means we need to slice preOrder[1 : 1 + 1] because of python slicing. And we need to slice inOrder[ : mid] because we don't need to include the mid(rootNode) in the inOrder traversal

    # 3. Create left & right Subtree with the sliced array
    root.left = self.buildTree(preorder[1 : mid + 1], inorder[ : mid])
    root.right = self.buildTree(preorder[mid + 1 : ], inorder[mid + 1 : ])

    # 4. Return root node
    return root


