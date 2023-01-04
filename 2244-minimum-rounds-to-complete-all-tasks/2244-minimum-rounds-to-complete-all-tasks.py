class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        m = {}
        
        for task in tasks:
            if task not in m:
                m[task] = 1
            else:
                m[task] += 1
        
        result = 0
        
        for i in m.values():

            k = i // 3
            r = i % 3
            
            if k == 0 and r == 1:
                return -1
            elif k == 0 and r == 2:
                result += 1
            else:
                if r == 0:
                    result += k
                elif r == 1:
                    result += (k - 1 + 2)
                else:
                    result += (k + 1)
                    
        return result
            