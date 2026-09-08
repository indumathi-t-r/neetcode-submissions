class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = prices[0]
        maxprofit = 0

        for i in prices:
            maxprofit = max(maxprofit, i-minbuy)
            minbuy = min(minbuy,i)
        return maxprofit