class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        remaining = 1
        m, n = len(grid), len(grid[0])
        x, y = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    remaining += 1
                elif grid[i][j] == 1:
                    x, y = i, j
       

        self.result = 0  
        # print(remaining)
        
        def bfs(x,y,remaining):
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] < 0:
                return
            
            if grid[x][y] == 2: #and remaining == 0:
                self.result += remaining == 0
                return
            
            grid[x][y] = -2
            bfs(x - 1, y, remaining - 1)
            bfs(x, y - 1, remaining - 1)
            bfs(x + 1, y, remaining - 1)
            bfs(x, y + 1, remaining - 1)
            grid[x][y] = 0
        
        bfs(x,y,remaining)
        
        return self.result