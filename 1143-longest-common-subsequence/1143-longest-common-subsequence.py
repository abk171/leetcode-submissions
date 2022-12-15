class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        l1 = len(text1)
        l2 = len(text2)

        M = [[0 for _ in range(l1 + 1)] for _ in range(l2 + 1)]

        for i in range(1,l2 + 1):
            for j in range(1,l1 + 1):
                if text2[i-1] == text1[j-1]:
                    M[i][j] = 1 + M[i-1][j-1]
                else:
                    M[i][j] = max(M[i-1][j], M[i][j-1])


        return M[-1][-1]
        