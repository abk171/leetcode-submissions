import queue

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        low = 1
        high = max(time) * totalTrips
        
        def numberOfTrips(x):
            s = 0
            for i in time:
                s += x // i
            return s
        
        while low < high:
            mid = (low + high) // 2
            if numberOfTrips(mid) >= totalTrips:
                high = mid
            else:
                low = mid + 1
            
        return low
             
                
        