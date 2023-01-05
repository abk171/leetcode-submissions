class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def gcd(a,b):
            if a < b:
                return gcd(b,a)
            if a == b:
                return a
            while b:
                a, b = b, a % b
            return a
        g = nums[0]
        for i in range(1, len(nums)):
            g = gcd(nums[i], g)
        return g == 1