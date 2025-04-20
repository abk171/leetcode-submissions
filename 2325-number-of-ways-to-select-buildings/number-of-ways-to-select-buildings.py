class Solution:
    def numberOfWays(self, s: str) -> int:
        total_zero = 0
        total_one = 0

        for c in s:
            if c == '0':
                total_zero += 1
            else:
                total_one += 1
        
        left_zero = 0
        left_one = 0

        result = 0
        for c in s:
            if c == '0':
                total_zero -= 1 
                left_zero += 1
                result += left_one * total_one
            else:
                total_one -= 1
                left_one += 1
                result += left_zero * total_zero
        return result
