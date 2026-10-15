class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # knowing the length of list is at least 2: we can initialize the list i think this will be helpful
        
        res = []
        
        product = 1

        z = []
        for i in range(len(nums)):
            if nums[i] == 0:
                z.append(i) 
                product *= 1
            else:
                product *= nums[i]

        if len(z) > 1:
            for i in range(len(nums)):
                res.append(0)

        elif len(z) == 1:
            for i in range(len(nums)):
                if i == z[0]:
                    res.append(product)
                else:
                    res.append(0)

        else :
            for n in nums:
                if n != 0:
                    res.append(product//n)

        return res

        # if there is 1 0 everything will be 0 except itself:
        # if there is > 1 0 eveyrthing will be 0
        # if there is no zeros the divide method works, we can not do that by 
        



        #     p *= n

        # 
        
        # res = []

        # for n in nums:
        #     if n != 0:
        #         res.append(p//n)
            
        
        # return res



        