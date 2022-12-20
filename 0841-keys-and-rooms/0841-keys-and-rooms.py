import queue
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = queue.Queue()
        q.put(0)
        
        visited = [False for _ in range(len(rooms))]
        
        while not q.empty():
            x = q.get()
            for y in rooms[x]:
                if not visited[y]:
                    q.put(y)
            visited[x] = True
            
        for v in visited:
            if not v:
                return False
        return True