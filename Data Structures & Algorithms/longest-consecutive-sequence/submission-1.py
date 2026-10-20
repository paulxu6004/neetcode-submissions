class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        cons = {}

        for num in nums:
            if num in cons:
                continue

            elif num - 1 in cons and num + 1 in cons:
                merged = cons[num - 1] + [num] + cons[num + 1]

            elif num - 1 in cons:
                merged = cons[num - 1] + [num]
                
            elif num + 1 in cons:
                merged = [num] + cons[num + 1]

            else:
                merged = [num]
                
            cons[merged[0]] = merged                        
            cons[merged[-1]] = merged                        
            cons[num] = merged

        
        
        return max((len(v) for v in cons.values()))
        


            



        