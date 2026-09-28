class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        sol = []
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        for i in range(k):
            best = max(count, key=count.get) 
            sol.append(best)
            count.pop(best)
        return sol        


        