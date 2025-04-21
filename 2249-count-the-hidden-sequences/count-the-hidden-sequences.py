class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        mini = 0
        maxi = 0
        cur = 0

        for i in differences:
            cur = cur + i
            mini = min(mini, cur)
            maxi = max(maxi, cur)

        result = (upper - lower + 1) - (maxi - mini) 
        return result if result > 0 else 0
