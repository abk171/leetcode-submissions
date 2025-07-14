class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]
        j = 0
        up = True
        
        for c in s:
            if j == numRows - 1:
                up = False
            if j == 0:
                up = True
            
            rows[j].append(c)
            j = j + 1 if up else j - 1
        
        return ''.join(''.join(row) for row in rows)