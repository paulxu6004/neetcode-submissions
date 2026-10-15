class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # knowing the length of list is at least 2: we can initialize the list i think this will be helpful
        
        zero_count = 0
        zero_index = -1
        product = 1

        for i, num in enumerate(nums):
            if num == 0:
                zero_count += 1
                zero_index = i
            else:
                product *= num

        if zero_count > 1:
            return [0] * len(nums)

        if zero_count == 1:
            res = [0] * len(nums)
            res[zero_index] = product
            return res

        
        return [product // num for num in nums]
        
        # if there is 1 0 everything will be 0 except itself:
        # if there is > 1 0 eveyrthing will be 0
        # if there is no zeros the divide method works, we can not do that by 
        




        