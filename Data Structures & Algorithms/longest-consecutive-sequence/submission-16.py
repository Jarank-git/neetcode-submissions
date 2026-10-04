class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        highest_cnt = 0

        if len(nums) == 0:
            return 0

        for i  in range(len(nums)):
            if nums[i] - 1 not in s:
                cnt = 0
                for j in range(len(nums)):
                    if nums[i] + j in s:
                        cnt +=1
                    else:
                        break
                if cnt > highest_cnt:
                    highest_cnt = cnt
                
                
        
        return highest_cnt
