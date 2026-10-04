class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        highest_cnt = 0


        for n in s:
            if n - 1 not in s:
                cnt = 0
                for j in range(len(nums)):
                    if n + j in s:
                        cnt +=1
                    else:
                        break
                if cnt > highest_cnt:
                    highest_cnt = cnt
                
                
        
        return highest_cnt
