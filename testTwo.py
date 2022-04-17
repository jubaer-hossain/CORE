class Solution:
    def getDirections(self, root, startValue, destValue):
        startPath, destPath = [], []

        self.getPath(root, startValue, startPath)
        self.getPath(root, destValue, destPath)

        while len(startPath) > 0 and len(destPath) > 0 and startPath[-1] == destPath[-1]:
            startPath.pop()
            destPath.pop()

        return "".join("U" * len(startPath)) + "".join(reversed(destPath))

    def getPath(self, node, targetValue, currentPath):
        if node.val == targetValue:
            return True

        # Bottom up recursive. Only returns at the end
        if node.left is not None and self.getPath(node.left, targetValue, currentPath):
            currentPath += "L"
        elif node.right is not None and self.getPath(node.right, targetValue, currentPath):
            currentPath += "R"
        return currentPath # Returns only once