class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        k_list = []


        # for num in nums:
        #     if len(k_list) < k:
        #         if len(k_list) == 0:
        #             k_list.append(num)
        #         elif num > k_list[-1]
        #             num.


        s = sorted(nums)
        return s[len(s) - k]
            

            
        