class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.backtrack(result, '', 0, 0, n)
        return result
        
        
    def backtrack(self, result, curr, left, right, n):
        if len(curr) == 2 * n:
            result.append(curr)
        
        if left < n:
            curr += '('
            self.backtrack(result, curr, left + 1, right, n)
            curr = curr[:-1]
        
        if right < left:
            curr += ')'
            self.backtrack(result, curr, left, right + 1, n)
            curr = curr[:-1]