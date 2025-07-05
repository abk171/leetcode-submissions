class Solution:
    def findLucky(self, arr: List[int]) -> int:
        frequencies = [0 for _ in range(501)]
        for i in arr:
            frequencies[i] += 1
        for i in range(500, 0, -1):
            if frequencies[i] == i:
                return frequencies[i]
        return -1