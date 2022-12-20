class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = [""]
        for i in range(10):
            s = str(i) * 3
            if s in num:
                result.insert(0,s)
        return result[0]
            