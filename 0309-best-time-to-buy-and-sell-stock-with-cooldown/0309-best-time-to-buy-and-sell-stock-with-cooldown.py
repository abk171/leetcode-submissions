class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        s = [0, -prices[0], -1001]
        
        for i in range(1, size):
            s0 = max(s[0], s[2])
            s1 = max(s[1], s[0] - prices[i])
            s2 = s[1] + prices[i]
            
            s = [s0, s1, s2]
            
        return max(s[0], s[2])