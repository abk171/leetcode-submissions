class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        count = [0 for _ in range(n)]
        
        for t in trust:
            a, b = t
            count[a - 1] -= 1
            count[b - 1] += 1
        
        print(count)
        for i, c in enumerate(count):
            if c == n - 1:
                return i + 1
        return -1