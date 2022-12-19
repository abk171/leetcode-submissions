class Solution:
    def dfs(self, i, j, grid):
        if i == len(grid):
            return j
        
        if grid[i][j] == 1:
            if j + 1 < len(grid[0]) and grid[i][j+1] != -1:
                return self.dfs(i+1,j+1,grid)
            else:
                return -1
        
        else:
            if j - 1 > -1 and grid[i][j-1] != 1:
                return self.dfs(i+1,j-1,grid)
            else:
                return -1
        
    def findBall(self, grid: List[List[int]]) -> List[int]:
        result = []
        for i in range(len(grid[0])):
            result.append(self.dfs(0,i,grid))
        return result