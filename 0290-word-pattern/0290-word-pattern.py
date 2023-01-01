class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        w2c = {}
        chars = set()
        
        for word, c in zip(words, pattern):
            # print(w2c)
            if word not in w2c and c not in chars:
                w2c[word] = c
                chars.add(c)
            elif word in w2c and w2c[word] != c:
                return False
            elif word not in w2c and c in chars:
                return False
        return True