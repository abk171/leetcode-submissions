class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack():
            if len(subset) == len(nums):
                result.append(subset[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in subset:
                    continue
                subset.append(nums[i])
                backtrack()
                subset.pop()
        backtrack()
        return result