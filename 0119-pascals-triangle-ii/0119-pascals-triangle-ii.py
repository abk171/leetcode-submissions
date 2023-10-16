class Solution:
    def getRow(self, n: int) -> List[int]:
        if n == 0:
            return [1]
        elif n == 1:
            return [1,1]
        else:
            prev = [1,1]
            next = [1 for _ in range(3)]
            
            for i in range(2,n + 1):
                for j in range(1,len(next) - 1):
                    next[j] = prev[j-1] + prev[j]
                prev = next
                next = [1 for _ in range(len(prev) + 1)]
            
            return prev
            