import queue

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visited = [False for _ in range(n)]
        q = queue.Queue()
        q.put(source)
        
        while not q.empty() and not visited[destination]:
            x = q.get()
            for y in adj[x]:
                if not visited[y]:
                    q.put(y)
            visited[x] = True
        
        return visited[destination]