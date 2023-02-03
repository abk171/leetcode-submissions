class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        answer = ["" for _ in range(numRows)]
        mod = numRows * 2 - 2
        
        for i, c in enumerate(s):
            y = i % mod
            if y < numRows:
                answer[y] += (c)
            else:
                answer[-1*(y - numRows) - 2] += (c)
        
        result = ""
        
        for i in answer:
            result += i
        
        return result