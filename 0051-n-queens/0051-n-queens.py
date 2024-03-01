import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [-1 for _ in range(n)]
        sols = []
        self.queens(cols, 0, sols)

        return self.transformer(sols,n)

    def transformer(self, sols,n):
        result = []
        for sol in sols:
            starr = []
            for i in sol:
                st = ['.']*n
                st[i] = 'Q'
                starr.append(''.join(st))
            result.append(starr)
        return result
    
    def queens(self, cols, i, sols):
        n = len(cols)
        if i == n:
            sols.append(copy.deepcopy(cols))

        
        for j in range(n):
            if self.promising(cols, i, j):
                cols[i] = j
                self.queens(cols, i + 1, sols)
    
    
    def promising(self, cols, i, j):
        if i == 0:
            return True
        for k in range(i):
            if cols[k] == j or abs(cols[k] - j) == abs(i - k):
                return False
        return True