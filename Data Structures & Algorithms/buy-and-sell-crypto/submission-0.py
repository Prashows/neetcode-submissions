class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit=0
        buy =prices[0]

        for data in prices:

            buy = min(data, buy)

            profit  =  max(profit, data - buy)
        return profit
             