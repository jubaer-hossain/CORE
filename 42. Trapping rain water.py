# O(n) time | O(1) space
def trap(self, height):
    left, right = 0, len(height) - 1
    leftMaxHeight, rightMaxHeight = height[left], height[right]
    result = 0

    while left < right:
        if leftMaxHeight < rightMaxHeight:
            left += 1
            leftMaxHeight = max(leftMaxHeight, height[left])
            result += leftMaxHeight - height[left]
            # So the formula to calculate how much water we can trap for each block is basically min(leftMaxHeightHeight, rightMaxHeightHeight) - currentHeight.

            # Since we entered into the leftMaxHeight "if statement" because leftMaxHeight is the minimum between leftMaxHeight and rightMaxHeight, there is no reason to calculate the entire formula.

            # We can only add the currentBlockWater to result and it is guaranteed to have a non-negative value
        else:
            right -= 1
            rightMaxHeight = max(rightMaxHeight, height[right])
            result += rightMaxHeight - height[right]

    return result

    