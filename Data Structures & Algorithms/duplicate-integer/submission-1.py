class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return False
        nums1 = set()
        for num in nums:
            if num in nums1:
                return True
            
            else:
                nums1.add(num)

        return False
            

        