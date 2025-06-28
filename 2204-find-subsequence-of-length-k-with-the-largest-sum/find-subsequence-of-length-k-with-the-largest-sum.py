class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        h = []
        for i, e in enumerate(nums):
            if len(h) < k:
                heapq.heappush(h,[e, i])
            else:
                heapq.heappushpop(h,[e, i])
        
        h.sort(key=lambda x: x[1])
        result = []
        for i in range(len(h)):
            result.append(h[i][0])
        
        return result