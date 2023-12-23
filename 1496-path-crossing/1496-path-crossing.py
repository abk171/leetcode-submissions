class Solution:
    def isPathCrossing(self, path: str) -> bool:
        past = set()
        updates = {
            'N': (0, 1),
            'E': (1, 0),
            'S': (0, -1),
            'W': (-1, 0)
        }
        x = 0
        y = 0
        
        past.add('0,0')
        
        for c in path:
            dx, dy = updates[c]
            x += dx
            y += dy
            p = str(x) + ',' + str(y)
            
            if p in past:
                return True
            else:
                past.add(p)
        return False
        