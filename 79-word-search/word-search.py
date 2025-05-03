class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtrack(r, c, i):
            if i == len(word):
                return True
            
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = '0'  # mark visited

            dr = [0, -1, 0, 1]
            dc = [-1, 0, 1, 0]

            for delr, delc in zip(dr, dc):
                nr, nc = r + delr, c + delc
                if backtrack(nr, nc, i + 1):
                    return True

            board[r][c] = temp  # unmark
            return False

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and backtrack(r, c, 0):
                    return True

        return False
