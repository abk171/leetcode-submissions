class disjointSet:
    def __init__(self):
        self.parent = [i for i in range(26)]
        
    def find(self, i):
        if i == self.parent[i]:
            return i
        else:
            return self.find(self.parent[i])
    
    def join(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        
        if pa != pb:
            ## join them on the basis of whose parent has the smallest index
            if pa < pb:
                self.parent[pb] = self.parent[pa]
            else:
                self.parent[pa] = self.parent[pb]
        
        

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        ds = disjointSet()
        a = ord('a')
        for i, j in zip(s1, s2):
            ds.join(ord(i) - a, ord(j) - a)
        
        result = ''
        for i in baseStr:
            result += chr(ds.find(ord(i) - a) + a)
        
        return result