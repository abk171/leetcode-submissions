class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        pmap = defaultdict(int)
        smap = defaultdict(int)
        
        sl = len(s)
        pl = len(p)
        
        for i in range(pl):
            sc = s[i]
            pc = p[i]
            
            pmap[pc] += 1
            smap[sc] += 1
        
        result = []
        if pmap == smap:
            result.append(0)
        
        for i in range(pl, sl):
            smap[s[i]] += 1
            if smap[s[i - pl]] == 1:
                del smap[s[i - pl]]
            else:
                smap[s[i - pl]] -= 1
            if smap == pmap:
                result.append(i - pl+1)
        
        return result
                