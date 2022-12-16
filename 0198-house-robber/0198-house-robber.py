class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        evenSum = 0
        oddSum = 0
        
        for i, v in enumerate(nums):
            if i % 2 == 0:
                evenSum += v
                evenSum = max(evenSum, oddSum)
            else:
                oddSum += v
                oddSum = max(evenSum, oddSum)           
        
        return max(evenSum,oddSum)
        