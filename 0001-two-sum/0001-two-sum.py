class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = {}
        for i,v in enumerate(nums):
            diff = target - v
            if diff in s:
                return [i,s[diff]]
            else:
                s[v] = i
        