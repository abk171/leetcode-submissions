import queue
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        apples = []
        for i,apple in enumerate(hasApple):
            if apple:
                apples.append(i)
        
#         distances = [float('inf') for _ in range(n)]
#         distances[0] = 0
#         parent = [i for i in range(n)]
        
#         q = queue.PriorityQueue()
#         for i, distance in enumerate(distances):
#             q.put((distance, i))
        
#         visited = [False for _ in range(n)]
        
#         while not q.empty():
#             distance, x = q.get()
#             for y in adj[x]:
#                 if distances[y] > 1 + distance:
#                     distances[y] = 1 + distance
#                     parent[y] = x
#                     q.put((distances[y], y))
#             visited[x] = True

        parent = [i for i in range(n)]
        visited = [False for _ in range(n)]
        
        def dfs(i):
            visited[i] = True
            for y in adj[i]:
                if not visited[y]:
                    dfs(y)
                    parent[y] = i

        
        dfs(0)
        
        visited_edges = set()
        
        def find(i):
            while i != 0:
                visited_edges.add((i, parent[i]))
                visited_edges.add((parent[i], i))
                i = parent[i]
        
        for apple in apples:
            find(apple)
        
        
        
        return len(visited_edges)
                    