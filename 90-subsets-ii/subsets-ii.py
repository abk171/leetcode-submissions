class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        nums.sort()

        

        def backtrack(start): 
            result.append(subset[:])  # add current subset
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue  # skip duplicates
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()

        backtrack(0)
        return result

            
            