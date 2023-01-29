class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        result = [0 for _ in range(n + 1)]
        
        result[0] = cost[0]
        result[1] = cost[1]
        
        
        for i in range(2, n+1):
            minv = min(result[i - 1], result[i - 2])
            result[i] = minv + cost[i] if i < n else minv
        
        return result[-1]
                
        