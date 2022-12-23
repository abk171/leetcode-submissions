class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        size = len(prices)
        profit = 0
        
        for i in range(1, size):
            if prices[i] < min:
                min = prices[i]
            else:
                profit = max(profit, prices[i] - min)
                
        return profit