# O(n) time | O(n) space
class Solution(object):
    def twoSum(self, nums, target):
        hashMap = {}
        for idx, num in enumerate(nums):
            currentDiff = target - num
            if currentDiff in hashMap: # Looking the other number of the current number to create targetSum in hashmap
                return [hashMap[currentDiff], idx]
            hashMap[num] = idx


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]] 

                   