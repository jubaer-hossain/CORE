class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums) # O(n) space time
        sequenceLength = 0

        for number in nums: # O(n) time
            if (number - 1) not in numSet: # No previous available - Start of a sequence
                currentLength = 0
                
                while (number + currentLength) in numSet: # O(n) time. Looking 1, 2, 3, 4...
                    currentLength += 1
                sequenceLength = max(currentLength, sequenceLength)
        
        return sequenceLength


