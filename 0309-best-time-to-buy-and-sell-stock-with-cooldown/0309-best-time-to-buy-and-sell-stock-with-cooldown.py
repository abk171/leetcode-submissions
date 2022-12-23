class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        s0 = [0 for _ in range(size)]
        s1 = [0 for _ in range(size)]
        s2 = [0 for _ in range(size)]
        
        s0[0] = 0
        s1[0] = -prices[0]
        s2[0] = -1001
        
        for i in range(1, size):
            s0[i] = max(s0[i - 1],s2[i - 1])
            s1[i] = max(s1[i - 1],s0[i - 1] - prices[i])
            s2[i] = s1[i - 1] + prices[i]
            
        return max(s0[-1], s2[-1])
        
        