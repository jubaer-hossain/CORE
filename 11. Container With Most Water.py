# O(n) time | O(n) space
def maxArea(self, height):
    left, right = 0, len(height) - 1
    finalArea = 0
    
    while left < right:
        currentArea = (right - left) * min(height[left], height[right])
        finalArea = max(finalArea, currentArea)

        if height[left] < height[right]:
            left += 1
        else: # Doesn't really matter if they are equal. We shift the right
            right -= 1
    return finalArea

