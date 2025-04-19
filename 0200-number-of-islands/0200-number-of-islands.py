class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        

        def explore(x, y):
            if x < 0 or y < 0 or x >= n or y >= m:
                return

            if grid[y][x] == '0':
                return
            
            grid[y][x] = '0'

            delx = [-1, 0, 1, 0]
            dely = [0, -1, 0, 1]

            for dx, dy in zip(delx, dely):
                    explore(x + dx, y + dy)
        
        count = 0
        
        for x in range(n):
            for y in range(m):
                if grid[y][x] == '0':
                    continue
                explore(x, y)
                count += 1
                
        return count