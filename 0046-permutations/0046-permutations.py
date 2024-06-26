class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        n = len(nums)
        
        def backtrack(i):
            if i >= n:
                result.append(nums[:])
            
            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i + 1)
                nums[i], nums[j] = nums[j], nums[i]
            
        backtrack(0)
        return result