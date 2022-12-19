class Solution:
    def sumOfSquares(self, n):
        sum = 0
        while n:
            sum += (n % 10)**2
            n = n//10
        return sum
        
    def isHappy(self, n: int) -> bool:
        s = set()
        
        while n != 1:
            if n in s:
                return False
            s.add(n)
            n = self.sumOfSquares(n)
        return True