class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        m = (r - l) * min(heights[l], heights[r])
        
        while l < r:
            if heights[l] < heights[r]:
                l += 1
                m = max(m, (r - l) * min(heights[l], heights[r]))
            elif heights[l] > heights[r]:
                r -= 1
                m = max(m, (r - l) * min(heights[l], heights[r]))
            else:
                l += 1
            
        
        return m
            
        