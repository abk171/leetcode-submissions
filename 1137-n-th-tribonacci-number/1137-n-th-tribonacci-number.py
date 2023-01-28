class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        soln = [0 for _ in range(n + 1)]
        soln[1] = 1
        soln[2] = 1
        
        for i in range(3, n + 1):
            soln[i] = soln[i - 1] + soln[i - 2] + soln[i - 3]
        
        return soln[-1]