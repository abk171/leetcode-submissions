class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix = [0 for _ in range(n)]
        w = 2 * k + 1
        
        for i, num in enumerate(nums):
            prefix[i] = prefix[i - 1] + num
        
        avgs = [-1 for _ in range(n)]
        
        for i in range(n):
            if i - k >= 0 and i + k < n:
                avgs[i] = (prefix[i + k] - prefix[i - k] + nums[i - k]) // w

        return avgs
                