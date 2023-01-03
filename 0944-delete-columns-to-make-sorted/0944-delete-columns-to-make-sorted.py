class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        dels = [False for _ in range(len(strs[0]))]
        for i in range(1,len(strs)):
            for j in range(len(strs[0])):
                if not dels[j] and strs[i-1][j] > strs[i][j]:
                    dels[j] = True
        for c in dels:
            if c:
                count += 1
        return count