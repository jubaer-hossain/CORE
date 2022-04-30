class Solution(object):
    def threeSum(self, nums):
    	res = []
    	nums.sort()
    	
    	for i in range(len(nums)):
    		if nums[i] > 0:
    			break
    		
    		if i == 0 or nums[i] != nums[i - 1]: # Calling twoSum only if the numbers are not duplicate
                print(seen)
    			self.twoSum(nums, res, i)
    	
    	return res
    	
    def twoSum(self, nums, res, i):
    	seen = set()
    	j = i + 1
    	
    	while j < len(nums):
    		complement = -(nums[i] + nums[j])
    		
    		if complement in seen:
    			res.append([nums[i], nums[j], complement])
    			
    			while j + 1 < len(nums) and nums[j] == nums[j + 1]: # Here we increment j to its last occurance. To avoid index error we put the checker that j is alws less than the lengh of the array
    				j += 1
    			
    		# Now we are at the last occurance of nums[j] once we exit the while loop
    		seen.add(nums[j])
    		j += 1

