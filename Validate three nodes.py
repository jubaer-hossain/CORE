# O(h) time | O(1) space
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # 1. If nodeOne is an ancestor of nodeTwo and nodeTwo is an ancestor of nodeThree then True
    if isDescendant(nodeOne, nodeTwo):
        return isDescendant(nodeTwo, nodeThree)

    # 2. The opposite case: if nodeThree is an ancestor of nodeTwo and nodeTwo is an ancestor of nodeOne then True
    if isDescendant(nodeThree, nodeTwo):
        return isDescendant(nodeTwo, nodeOne)

    # 3. If none of the above is true then they are not in a same ancestor tree/path
    return False

# O(h) time | O(1) space because of the BST property
def isDescendant(ancestorNode, descendantNode):
    # Basically in every iteration we are moving closer towards the descendantNode using the BST property
    while ancestorNode is not None and ancestorNode is not descendantNode:
        if descendantNode.value < ancestorNode.value:
            ancestorNode = ancestorNode.left
        else:
            ancestorNode = ancestorNode.right

    # Ancestor node could be None. This verifies that
    return ancestorNode is descendantNode

# O(h) time | O(1) space because of the BST property
def isDescendant(parentNode, childNode):
    # Basically in every iteration we are moving closer towards the descendantNode using the BST property
    while parentNode is not None and parentNode is not childNode:
        if childNode.value < parentNode.value:
            parentNode = parentNode.left
        else:
            parentNode = parentNode.right

    # Ancestor node could be None. This verifies that
    return parentNode is childNode





# O(d) time | O(1) space - where d is the distance between nodeOne and nodeThree
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # 1. Start searching from nodeOne and nodeThree and try to find nodeTwo
    searchOne = nodeOne
    searchThree = nodeThree

    # 2. Continue the search until you find nodeTwo or nodeOne reached to nodeThree or vice verca or both nodes reaches to the end
    while True:
        foundOneFromAnother = searchOne is nodeThree or searchThree is nodeOne
        foundTwo = searchOne is nodeTwo or searchThree is nodeTwo
        endOfSearch = searchOne is None and searchThree is None

        if foundOneFromAnother or foundTwo or endOfSearch:
            break

        # 2.1. Basically traversing the BST and assigning either left or right based on the values
        if searchOne is not None:
            searchOne = searchOne.left if searchOne.value > nodeTwo.value else searchOne.right
        if searchThree is not None:
            searchThree = searchThree.left if searchThree.value > nodeTwo.value else searchThree.right

    # 3. Seeing why we broke out of the loop? Is it because either nodeThree or nodeOne found nodeTwo or they found each other
    foundOneFromAnother = searchOne is nodeThree or searchThree is nodeOne
    foundNodeTwo = searchOne is nodeTwo or searchThree is nodeTwo

    # 4. If nodeTwo is not Found or they found each other(means nodeTwo is not in this path), then definitely false
    if not foundNodeTwo or foundOneFromAnother:
        return False

    # 5. Check ancestors: Either nodeOne or nodeThree is a descendant from nodeTwo
    descendantFromTwo = nodeThree if searchOne is nodeTwo else nodeOne
    
    return isDescendant(nodeTwo, descendantFromTwo)


# O(h) time | O(1) space because of the BST property
def isDescendant(parentNode, childNode):
    while parentNode is not None and parentNode is not childNode:
        if childNode.value < parentNode.value:
            parentNode = parentNode.left
        else:
            parentNode = parentNode.right

    # Ancestor node could be None. This verifies that
    return parentNode is childNode



