import queue
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        cost = [[] for _ in range(n)]
        
        mod = 10 ** 9 + 7
        
        for road in roads:
            adj[road[0]].append(road[1])
            adj[road[1]].append(road[0])
            cost[road[0]].append(road[2])
            cost[road[1]].append(road[2])
            
        distances = [float('inf') for _ in range(n)]
        distances[0] = 0
        ways = [0 for _ in range(n)]
        ways[0] = 1
        
        pq = queue.PriorityQueue()
        
        
        visited = [False for _ in range(n)]
        
        for i, distance in enumerate(distances):
            pq.put((distance, i))
        
        while not pq.empty():
            x_distance, x_index = pq.get()
            for j,y in enumerate(adj[x_index]):
                if not visited[y]:
                    if distances[y] > x_distance + cost[x_index][j]:
                        distances[y] = x_distance + cost[x_index][j]
                        pq.put((distances[y], y))
                        ways[y] = ways[x_index] % mod
                    elif distances[y] == x_distance + cost[x_index][j]:
                        ways[y] = (ways[y] + ways[x_index]) % mod
                        
            visited[x_index] = True
            # print(distances)

                   
        return ways[-1]
        
            