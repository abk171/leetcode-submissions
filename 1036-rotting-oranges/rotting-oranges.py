class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        bfs = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    bfs.append((i, j)) # minute, row, column
                elif grid[i][j] == 1:
                    fresh += 1
        
        del_i = [0, -1, 0, 1]
        del_j = [-1, 0, 1, 0]
        
        total_time = 0

        while bfs:

            size = len(bfs)

            for _ in range(size):
                row, col = bfs.popleft()

                for di, dj in zip(del_i, del_j):
                    new_row = row + di
                    new_col = col + dj

                    if new_row < 0 or new_col < 0 or new_row >= m or new_col >= n:
                        continue
                    
                    if grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        bfs.append((new_row, new_col))
                        fresh -= 1
            
            if bfs:
                total_time += 1
        
        return total_time if fresh == 0 else -1