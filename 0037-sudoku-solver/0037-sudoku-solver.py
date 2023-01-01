class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def isPossible(x,y,num):
            for val in board[y]:
                if val == num:
                    return False
            for row in board:
                if row[x] == num:
                    return False
                
            s_x = x // 3
            s_y = y // 3
            
            for i in range(3*s_y, 3*s_y + 3):
                for j in range(3*s_x, 3*s_x + 3):
                    if board[i][j] == num:
                        return False
            
            return True
        
        def solve(x,y):
            if y == 9:
                return True
            if x == 9:
                return solve(0,y + 1)
            
            if board[y][x] != '.':
                return solve(x + 1, y)
            
            else:
                for i in range(1, 10):
                    if isPossible(x,y, str(i)):
                        board[y][x] = str(i)
                        if solve(x + 1,y): return True
                        board[y][x] = '.'
            return False
    
        solve(0,0)