class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        arrptr = len(num) - 1
        carry = 0
        while arrptr >= 0:
            s = num[arrptr] + k % 10 + carry
            num[arrptr] = s % 10
            carry = s // 10
            k = k // 10
            arrptr -= 1 


        while k > 0:
            s = k % 10 + carry
            num = [s % 10] + num
            carry = s // 10
            k = k // 10

        if carry > 0:
            num = [carry] + num
        
        return num
            
            
            