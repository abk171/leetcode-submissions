class disjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.connected = n
    
    def findRoot(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.findRoot(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        ip = self.findRoot(i)
        jp = self.findRoot(j)
        
        if ip == jp:
            return
        self.connected -= 1
        
        irank = self.rank[ip]
        jrank = self.rank[jp]
        
        if irank < jrank:
            self.parent[ip] = jp
        else:
            self.parent[jp] = ip
            if irank == jrank:
                self.rank[ip] += 1
        
        

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        s = disjointSet(n)
        
        for connection in connections:
            i, j = connection
            s.union(i, j)
        
        
        return s.connected - 1
        
        
            