class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                threeNumberSum = a + nums[left] + nums[right]
                if threeNumberSum < 0:
                    left += 1
                elif threeNumberSum > 0:
                    right -= 1
                else:
                    result.append([a, nums[left], nums[right]])
                    while nums[left] == nums[left + 1] and left < right:
                        left += 1
                    left += 1
        return result
