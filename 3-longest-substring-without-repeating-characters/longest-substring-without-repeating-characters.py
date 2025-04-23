class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            c = s[right]
            while c in m:
                m.remove(s[left])
                left += 1
            m.add(c)
            max_len = max(max_len, right - left + 1)
        
        return max(max_len, len(m))