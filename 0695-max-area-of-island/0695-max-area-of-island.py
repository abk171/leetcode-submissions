class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)
        
        visited = [[False for _ in range(m)] for _ in range(n)]
        
        maxArea = 0
        
        def findArea(i, j):
            if (i not in range(n)
               or j not in range(m)
               or visited[i][j]
               or grid[i][j] == 0):
                return 0
            
            visited[i][j] = True
            
            s = 1
            directions = [[0,1], [-1, 0], [0, -1], [1, 0]]
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                s += findArea(ni, nj)
            
            return s
    
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == 1:
                    maxArea = max(maxArea, findArea(i, j))
        
        return maxArea