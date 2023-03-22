class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        nodes = max([max(road[0], road[1]) for road in roads])
        
        adj = [[] for _ in range(nodes)]
        cost = [[] for _ in range(nodes)]
        
        for road in roads:
            x,y,d = road
            adj[x-1].append(y-1)
            adj[y-1].append(x-1)
            cost[x-1].append(d)
            cost[y-1].append(d)
        
        visited = [False for _ in range(nodes)]
        self.mind = 10 ** 5 + 1
        
        def bfs(node):
            if not visited[node]:
                visited[node] = True
                for x, c in zip(adj[node], cost[node]):
                    self.mind = min(self.mind, c)
                    bfs(x)
                
        
        bfs(0)
        return self.mind
                
                    