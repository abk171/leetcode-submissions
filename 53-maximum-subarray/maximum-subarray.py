class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, curSum = nums[0], 0
        for n in nums:
            curSum += n
            maxSum = max(maxSum, curSum)
            curSum = max(curSum, 0)

        return maxSum