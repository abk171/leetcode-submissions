import queue
class Solution:
    
    def bfs(self, source, color, adj):
        q = queue.Queue()
        q.put(source)
        color[source] = 1
        
        while not q.empty():
            x = q.get()
            c = color[x]
            for y in adj[x]:
                if color[y] == -1:
                    q.put(y)
                    color[y] = 2 if c == 1 else 1
                elif color[y] == c:
                    return False
        return True
    
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for d in dislikes:
            adj[d[0] - 1].append(d[1] - 1)
            adj[d[1] - 1].append(d[0] - 1)
        
        color = [-1 for _ in range(n)]
        
        for i in range(n):
            if color[i] == -1:
                if not self.bfs(i, color, adj):
                    return False
                
        return True
            
        
        
                    