class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        totalLoad = sum(weights)
        maxLoad = max(weights)
        
        def feasible(weights, cap, days):
            daycap = cap
            i = 0
            while days > 0 and i < len(weights):
                if daycap >= weights[i]:
                    daycap -= weights[i]
                    i += 1
                else:
                    daycap = cap
                    days -= 1
            
            if i == len(weights):
                return True
            return False
        
        low = maxLoad
        high = totalLoad
        
        mid = (low + high) // 2
        
        while low < high:
            mid = (low + high) // 2
            if feasible(weights, mid, days):
                high = mid
            else:
                low = mid + 1
        
        return low