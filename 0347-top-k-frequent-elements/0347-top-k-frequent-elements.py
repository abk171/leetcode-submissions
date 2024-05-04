import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        h = []
        for key in d:
            heapq.heappush(h, (-1 * d[key], key))
        
        result = []
        for j in range(k):
            _, e = heapq.heappop(h)
            result.append(e)
        
        return result
        