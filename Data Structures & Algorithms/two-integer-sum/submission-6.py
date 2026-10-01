class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}
        for i, num in enumerate(nums):
            map1[num] = i
        for j, num in enumerate(nums):
            if ((target - num) in map1) and map1[target - num] != j:
                return [min(map1[target - num], j), max(map1[target - num], j)]
        return []

        