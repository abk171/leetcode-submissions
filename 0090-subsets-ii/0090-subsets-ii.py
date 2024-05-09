class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        
        result = []

        
        def backtrack(i, subset):
            if i >= n:
                result.append(subset.copy())
                return
                
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
            
            # subset.append(nums[i])
            backtrack(i + 1, subset)
            # subset.pop()
        
        backtrack(0, [])
        return result