# O(n^2) time | O(1) space
class Solution(object):
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        
        


# O(n) time | O(1) space
class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1

        while left < right:
            currentSum = numbers[left] + numbers[right]
            if currentSum < target:
                left += 1
            elif currentSum > target:
                right -= 1
            else:
                return [left + 1, right + 1]


        