class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1 
        maxarea = 0
        
        while i < j:
            #print(i,j)
            maxarea = max(maxarea,min(heights[i],heights[j]) * (j-i))
            #print(maxarea)
            if heights[i] < heights[j]:
                i = i + 1
            else:
                j = j - 1
        return maxarea

            

        


            
        