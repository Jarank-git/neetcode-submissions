class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pntr1 = 0
        pntr2 = len(numbers) - 1

        for i in range(len(numbers)):
            sum = numbers[pntr1] + numbers[pntr2]
            if sum == target:
                break
            elif sum < target:
                pntr1 += 1
            else:
                pntr2 -= 1

        result = [pntr1 + 1, pntr2 + 1]    
        return result
        