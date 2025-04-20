class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]

        # 101
        count = 0
        for i, c in enumerate(s):
            if c == '0':
                left[i] = count
            else:
                count += 1
        
        count = 0
        for i in range(n - 1, -1, -1):
            c = s[i]
            if c == '0':
                right[i] = count
            else:
                count += 1
        
        m1 = 0
        for i in range(n):
            m1 += left[i] * right[i]
        
        # 010
        count = 0
        for i, c in enumerate(s):
            left[i] = 0
            if c == '1':
                left[i] = count
            else:
                count += 1
        
        count = 0
        for i in range(n - 1, -1, -1):
            c = s[i]
            right[i] = 0
            if c == '1':
                right[i] = count
            else:
                count += 1
        
        m2 = 0
        for i in range(n):
            m2 += left[i] * right[i]

        return m1 + m2