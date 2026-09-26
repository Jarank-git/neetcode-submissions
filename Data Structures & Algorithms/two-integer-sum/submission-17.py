class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cnt = {}

        for c in range(len(nums)):
            cnt[nums[c]] = c

        for i in range(len(nums)):
            num_Need = target - nums[i]
            if num_Need in cnt and i != cnt.get(num_Need):
                ans = []
                ans.append(i)
                ans.append(cnt.get(num_Need))
                return ans
        

            