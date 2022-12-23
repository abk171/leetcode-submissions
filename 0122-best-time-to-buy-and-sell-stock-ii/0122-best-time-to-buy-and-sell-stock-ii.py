class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        size = len(prices)
        
        for i in range(1, size):
            profit += 0 if prices[i] < prices[i - 1] else prices[i] - prices[i - 1]
            
        return profit