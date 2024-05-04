class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftPrefix = []
        rightPrefix = []
        n = len(nums)
        
        for i in range(n):
            if i == 0:
                leftPrefix.append(nums[i])
                rightPrefix.append(nums[n - i - 1])
            else:
                leftPrefix.append(nums[i] * leftPrefix[-1])
                rightPrefix.append(nums[n - i - 1] * rightPrefix[-1])
        
        rightPrefix.reverse()
        result = []
        for i in range(n):
            a = 1
            if i - 1 >= 0:
                a *= leftPrefix[i - 1]
            if i + 1 < n:
                a *= rightPrefix[i + 1]
            
            result.append(a)
        
        return result
        

    