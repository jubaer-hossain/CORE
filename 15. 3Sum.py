# Using the sorting and 
# O(n^2) time | O(n) space for sorting. O(1) if we use heapsort
class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: # For duplicate "a" value
                continue

            # Two sum function
            left, right = i + 1, len(nums) - 1
            while left < right:
                threeNumberSum = a + nums[left] + nums[right]

                if threeNumberSum < 0:
                    left += 1
                elif threeNumberSum > 0:
                    right -= 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1

                    # Pushing the left pointer until we find a unique value
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res

# Using hashset Two Sum function
# O(n^2) time | O(n) space 
class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i == 0 or nums[i] != nums[i - 1]:  # Calling twoSum only if the numbers are not duplicate
                self.twoSum(nums, res, i)

            return res

    def twoSum(self, nums, res,i,):
        seen = set()
        j = i + 1

        while j < len(nums):
            complement = -(nums[i] + nums[j])

            if complement in seen:
                res.append([nums[i], nums[j], complement])

                while j + 1 < len(nums) and nums[j] == nums[j + 1]:  # Here we increment j to its last occurance. To avoid index error we put the checker that j is alws less than the lengh of the array
                    j += 1

            # Now we are at the last occurance of nums[j] once we exit the while loop

            seen.add(nums[j])
            j += 1