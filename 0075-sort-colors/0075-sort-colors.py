class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0 for _ in range(3)]
        
        for i in range(3):
            count[i] = 0
        
        for el in nums:
            count[el] += 1
        
        c = 0
        for i in range(3):
            for j in range(count[i]):
                nums[c] = i
                c += 1
            