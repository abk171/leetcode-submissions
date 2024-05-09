class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        subset = []
        
        def backtrack(i):
            if i >= n:
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return result
    
    
            
            
            
            