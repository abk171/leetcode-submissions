class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        result = set()
        current = []
        
        def backtrack(index):
            if index == n:
                if len(current) >= 2:
                    result.add(tuple(current))
                return
            if not current or current[-1] <= nums[index]:
                current.append(nums[index])
                backtrack(index + 1)
                current.pop()
            
            backtrack(index + 1)
        
        backtrack(0)
        
        return result
        
                    