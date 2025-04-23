class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def simulate(speed):
            hours = 0 
            for i in range(len(piles)):
                hours += (piles[i] + speed - 1) // speed
                if hours > h:
                    return False

            return hours <= h

        start, end = 1, max(piles)
        result = end
        while start <= end:
            mid = (start + end) // 2
            if simulate(mid):
                end = mid - 1
                result = mid
            elif not simulate(mid):
                start = mid + 1

        
        return result
