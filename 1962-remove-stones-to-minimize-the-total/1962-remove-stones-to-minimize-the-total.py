import queue
import math
class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        q = queue.PriorityQueue()
        
        for pile in piles:
            q.put(-1 * pile)
            
        for _ in range(k):
            x = -1 * q.get()
            value = x - math.floor(x / 2)
            q.put(-1 * value)
        
        sum = 0
        while not q.empty():
            x = -1 * q.get()
            sum += x
        
        return sum
        
        