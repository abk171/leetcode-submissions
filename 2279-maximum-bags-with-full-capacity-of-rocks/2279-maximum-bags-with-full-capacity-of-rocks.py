class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remaining = []
        for cap, rock in zip(capacity, rocks):
            remaining.append(cap - rock)
        
        remaining.sort()
        
        i = 0
        while i < len(capacity) and additionalRocks > 0:
            if additionalRocks >= remaining[i]:
                additionalRocks -= remaining[i]
                i += 1
            else:
                return i
        
        return i