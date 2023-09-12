class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1
        print(cnt)
        nums = set()
        ctr = 0
        for c in cnt:
            n = cnt[c]
            while n in nums and n > 0:
                n -= 1
                ctr += 1
            nums.add(n)
        return ctr
        
        