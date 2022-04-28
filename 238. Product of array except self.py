class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums))

        prefix = 1

        # [1, 2, 3, 4]
        for i in range(len(nums)):
            result[i] = prefix # [1, 1, 2, 6]
            prefix *= nums[i] # 1, 2, 3. Use the nums array not the result array
        
        suffix = 1
        for i in reversed(range(len(nums))):
            result[i] *= suffix
            suffix *= nums[i] # Using the nums array not the result array
        
        return result