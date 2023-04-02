import queue
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = queue.Queue()
        q.put((sr, sc))
        m = len(image)
        n = len(image[0])
        scolor = image[sr][sc]
        
        if scolor == color:
            return image
        
        while not q.empty():
            x,y = q.get()
            if image[x][y] == scolor:
                image[x][y] = color
            else:
                continue
            
            if x-1 >= 0:
                q.put((x-1,y))
            if x+1 < m:
                q.put((x+1,y))
            if y-1 >= 0: 
                q.put((x,y-1))
            if y+1 < n:
                q.put((x,y+1))
        
        return image