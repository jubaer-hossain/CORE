class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        firstNumber = defaultdict(list)

        nums.sort()