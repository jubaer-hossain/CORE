# O(k) time | O(1) space
def maxScore(self, cardPoints, k):
    left, right = 0, len(cardPoints) - k # Here the "left" idx is the pointer outside the leftmost idx of the sliding window. It's not within the window. Rather 1 idx left of the actual sliding window
    currentTotal = sum(cardPoints[right:]) # Could take extra memory in python. Ask interviewer and if he is neatpicking then use a for loop
    result = currentTotal

    while right < len(cardPoints):
        currentTotal = currentTotal - cardPoints[right] + cardPoints[left]
        result = max(currentTotal, result)
        
        left += 1
        right += 1

    return result


