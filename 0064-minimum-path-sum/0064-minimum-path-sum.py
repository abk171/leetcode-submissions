import queue
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def getNeighbors(i, j):
            neighbors = []
            if i+1 < m:
                neighbors.append((i+1, j))
            if j+1 < n:
                neighbors.append((i, j+1))
            return neighbors
        
        distance = [[float('inf') for _ in range(n)] for _ in range(m)]
        distance[0][0] = grid[0][0]
        
        q = queue.PriorityQueue()
        
        for i in range(m):
            for j in range(n):
                q.put((distance[i][j], i , j))
        
        while not q.empty():
            node_distance, node_i, node_j = q.get()
            for neighbor_i, neighbor_j in getNeighbors(node_i, node_j):
                if node_distance + grid[neighbor_i][neighbor_j] < distance[neighbor_i][neighbor_j]:
                    distance[neighbor_i][neighbor_j] = node_distance + grid[neighbor_i][neighbor_j]
                    q.put((distance[neighbor_i][neighbor_j], neighbor_i, neighbor_j))
        
        return distance[-1][-1]
                
                