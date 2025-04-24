class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        result = 0

        for i in nums:
            if i - 1 in nums:
                continue
            j = i + 1
            while j in nums:
                j += 1
            
            result = max(result, j - i)
        
        return result