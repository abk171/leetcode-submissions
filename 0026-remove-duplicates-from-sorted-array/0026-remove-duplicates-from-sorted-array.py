class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 1
        cur = nums[0]
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != cur:
                k += 1
                cur = nums[i]
                nums[pos] = nums[i]
                pos += 1
        return k


