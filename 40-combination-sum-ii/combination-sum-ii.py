class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        print(candidates)
        
        result = []
        subset = []

        def backtrack(start, t):
            if t == 0:
                result.append(subset[:])
                return
            
            if t < 0:
                return

            for i in range(start, len(candidates)):
                n = candidates[i]
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(n)
                backtrack(i + 1, t - n)
                subset.pop()
                

        
        backtrack(0, target)
        return result