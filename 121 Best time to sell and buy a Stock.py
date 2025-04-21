class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leastpp = float('inf')
        maxP = 0
        for cp in prices:
            profit = cp - leastpp
            maxP = max(maxP, profit)
            leastpp=min(leastpp,cp)

        return maxP  
        