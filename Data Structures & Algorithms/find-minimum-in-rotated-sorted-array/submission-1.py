class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mi = nums[l]

        while l <= r:
            if nums[l] < nums[r]:
                mi = min(mi, nums[l])
                return mi
           
            m = (l + r)//2
            mi = min(mi, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1   
                
            else:
                r = m - 1
                
        
        return mi
