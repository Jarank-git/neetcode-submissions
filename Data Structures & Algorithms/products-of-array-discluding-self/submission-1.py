class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tmp_1 = 1
        tmp_2 = 1
        prefix = []
        suffix = []
        final_list = []
        
        #iterate right to left
        for i in range(len(nums) - 1, -1, -1):
            suffix.append(tmp_1)
            tmp_1 *= nums[i]
            
        # iterate left to right
        for i in range(len(nums)): 
            prefix.append(tmp_2)
            tmp_2 *= nums[i]
        
        # multiply each index together
        for i in range(len(nums)):
            tmp_3 = 1
            tmp_3 = prefix[i] * suffix[len(nums) - i - 1]
            final_list.append(tmp_3)

     
        return final_list

            

            
        