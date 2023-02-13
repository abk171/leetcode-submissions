class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (high - low + 1) & 1:
            return (high - low) // 2 + low % 2
        else:
            return (high - low + 1) // 2