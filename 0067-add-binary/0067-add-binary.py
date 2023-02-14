class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aptr = len(a) - 1
        bptr = len(b) - 1
        result = ""
        c = 0
        sum = 0
        
        while aptr >= 0 or bptr >= 0 or c == 1:
            sum = 0
            if aptr >= 0:
                sum += int(a[aptr])
                aptr -= 1
                
            if bptr >= 0:
                sum += int(b[bptr])
                bptr -= 1
            
            sum += c
            
            c = sum // 2
            sum = sum % 2
            
            result = str(sum) + result
        
        return result
            
                
            
            
            