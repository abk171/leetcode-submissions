import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        h = []
        for i in nums:
            heapq.heappush(h, i)
        
        seq = 1
        maxseq = 1
        prev = heapq.heappop(h)
        while h:
            cur = heapq.heappop(h)

            if cur - prev == 1:
                seq += 1
            elif cur - prev == 0:
                prev = cur
                continue
            else:
                seq = 1
            maxseq = max(maxseq, seq)
            prev = cur
            
        
        return maxseq