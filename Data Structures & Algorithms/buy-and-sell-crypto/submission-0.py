class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        b = prices[0]
        p = 0

        for n in prices:
            if n < b:
                b = n

            elif b < n:
                p = max(p, n - b)

        return p
            



        