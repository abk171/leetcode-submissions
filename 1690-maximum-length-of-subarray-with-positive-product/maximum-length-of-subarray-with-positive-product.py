class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        first_neg = -1
        neg_count = 0
        max_len = 0
        start = 0

        for i, num in enumerate(nums):
            if num == 0:
                start = i + 1
                first_neg = -1
                neg_count = 0
            else:
                if num < 0:
                    neg_count += 1
                    if first_neg == -1:
                        first_neg = i
                
                if neg_count % 2 == 0:
                    max_len = max(max_len, i - start + 1)
                else:
                    max_len = max(max_len, i - first_neg)
        
        return max_len
