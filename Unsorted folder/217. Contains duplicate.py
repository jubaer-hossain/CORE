# Sort the array
# Run for loop

# O(NlogN) time | O(1) space
def containsDuplicate(self, nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False

# Using a hashset to store previously found unique values
# O(n) time | O(n) space
def containsDuplicate(self, nums):
    uniqueValues = set() # Hashset

    for number in nums:
        if number in uniqueValues:
            return True
        uniqueValues.add(number)

    return False

# Super python approach
# Since set contains only unique values we can convert the list into a set and compare if both of their lenghts are equal. If equal then it doesn't contain duplicates. If not then it contains duplicate

# O(n) time | O(n) space
def containsDuplicate(self, nums):
    return not (len(set(nums)) == len(nums))