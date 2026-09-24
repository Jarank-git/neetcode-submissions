
class Solution:
    def hasDuplicate(self, nums):
        checked = set()
        for i in range (0, len(nums)):
            if (nums[i] in checked):
                return True
            checked.add(nums[i])    
        return False 

