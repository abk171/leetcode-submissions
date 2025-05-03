class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        candidates.sort()
        
        def backtrack(start, t):
            if t < 0 or start >= len(candidates):
                return
            if t == 0:
                result.append(subset.copy())
                return
            
            print(start, t, subset)
            
            n = candidates[start]
            
            subset.append(n)
            backtrack(start, t - n)
            subset.pop()
            backtrack(start + 1, t)    

        backtrack(0, target)
        return result    