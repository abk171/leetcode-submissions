class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        maxJump = 0
        for i, jump in enumerate(nums):
            if maxJump >= size - 1:
                return True
            if i <= maxJump:
                maxJump = max(maxJump, jump + i)
            else:
                return False