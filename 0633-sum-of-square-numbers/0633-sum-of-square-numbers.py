class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        s = set()
        
        for i in range(int(math.sqrt(c) + 1)):
            s.add(i ** 2)
        
        for i in s:
            if c - i in s:
                return True
        
        return False