class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid[0])
        n = len(grid)
        visited = [[False for _ in range(m)] for _ in range(n)]
        
        islands = 0
        
        def dfs(i, j):
            if i < 0 or i > n - 1 or j < 0 or j > m - 1 or grid[i][j] == "0" or visited[i][j]:
                return
            
            visited[i][j] = True
            
            directions = [[0, 1], [-1, 0], [0, -1], [1, 0]]
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                dfs(ni, nj)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i,j)
                    islands += 1
        print(visited)
        return islands
        