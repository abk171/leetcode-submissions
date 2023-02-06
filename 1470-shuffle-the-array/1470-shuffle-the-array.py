class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        xptr = 0
        yptr = n
        
        for i in range(n):
            result.append(nums[xptr])
            result.append(nums[yptr])
            xptr += 1
            yptr += 1
        
        return result