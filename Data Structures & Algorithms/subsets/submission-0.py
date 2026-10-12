class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def dfs(i, ss):
            if i == len(nums):
                result.append(ss.copy())
                return
            
            ss.append(nums[i])
            dfs(i+1, ss)
            ss.pop()
            dfs(i+1, ss)

        dfs(0, [])
        return result
        
                


        
            
        


        