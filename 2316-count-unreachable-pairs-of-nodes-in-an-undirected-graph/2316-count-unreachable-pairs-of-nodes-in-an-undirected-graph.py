class disjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    
    def find(self,i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self,i, j):
        pi = self.find(i)
        pj = self.find(j)
        
        if pi == pj:
            return
        
        ir = self.rank[pi]
        jr = self.rank[pj]
        
        if ir < jr:
            self.parent[pi] = pj
        else:
            if ir == jr:
                self.rank[pi] += 1
            self.parent[pj] = pi
            
    
    
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        s = disjointSet(n)
        for edge in edges:
            i, j = edge
            s.union(i, j)
        
        result = 0
        
        d = defaultdict(int)
        
        for i in range(n):
            d[s.find(i)] += 1
        
        exhausted = 0
        
        for key in d:
            val = d[key]
            exhausted += val
            rem = n - exhausted
            result += rem * val
            
        return result
        
        
            