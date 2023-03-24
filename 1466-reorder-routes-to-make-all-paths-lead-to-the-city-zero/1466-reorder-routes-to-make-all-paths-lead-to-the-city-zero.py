class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        
        
        for connection in connections:
            i, j = connection
            adj[i].append((j, True))
            adj[j].append((i, False))
            
            
        
        self.flips = 0
        visited = [False for _ in range(n)]
        def dfs(node):
            if not visited[node]:
                visited[node] = True
                for connection in adj[node]:
                    y, direction = connection
                    if not visited[y]:
                        if direction:
                            self.flips += 1
                        dfs(y)
        dfs(0)
        return self.flips
            