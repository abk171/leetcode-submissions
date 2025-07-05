class Solution:
    def findLucky(self, arr: List[int]) -> int:
        m = {}
        for i in arr:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1

        max_i = -1
        for i, freq in m.items():
            if freq == i and i > max_i:
                max_i = i
        

        return max_i