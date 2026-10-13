class Solution:
    def maxArea(self, heights: List[int]) -> int: 
        #index for each pointer
        pntr1 = 0
        pntr2 = len(heights) - 1
        current_max = 0
        for i in range(len(heights)):
    
            
            
        
            width = pntr2 - pntr1
            height = min(heights[pntr2], heights[pntr1])
            
            if height == heights[pntr1]:
                pntr1 +=1
            else:
                pntr2 -=1

            if height * width > current_max:
                current_max = height * width
        
        return current_max
           

            
        