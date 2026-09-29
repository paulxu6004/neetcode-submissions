class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return results
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] = frequency[num] + 1
            else:
                frequency[num] = 1

        sortednums = sorted(frequency, key=frequency.get, reverse=True)
        return sortednums[:k]