class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            pntr1 = i + 1
            pntr2 = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while pntr1 < pntr2:
                sum = nums[pntr1] + nums[pntr2] + nums[i]
                tmp = []
                if sum == 0:   
                    tmp.append(nums[pntr1])
                    tmp.append(nums[pntr2])
                    tmp.append(nums[i])
                    result.append(tmp)
                    pntr1 +=1
                    pntr2 -=1

                    while pntr1 < pntr2 and nums[pntr1] == nums[pntr1 - 1]:
                        pntr1 += 1

                    while pntr1 < pntr2 and nums[pntr2] == nums[pntr2 + 1]:
                        pntr2 -= 1

                elif sum < 0:
                    pntr1 +=1
                else:
                    pntr2 -=1
                   

        return result 