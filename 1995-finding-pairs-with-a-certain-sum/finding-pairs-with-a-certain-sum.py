class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums2_dict = {}

        for num in nums2:
            if num in self.nums2_dict:
                self.nums2_dict[num] += 1
            else:
                self.nums2_dict[num] = 1
        
        self.nums1 = sorted(self.nums1)

    def _first_occurrence(self, other):
        low, high = 0, len(self.nums1) - 1
        pos = -1
        while low <= high:
            mid = (low + high) // 2
            if self.nums1[mid] == other:
                pos = mid
                high = mid - 1
            elif self.nums1[mid] < other:
                low = mid + 1
            else:
                high = mid - 1
        return pos  

    def add(self, index: int, val: int) -> None:
        cur = self.nums2[index]
        new = cur + val

        if self.nums2_dict[cur] == 1:
            del self.nums2_dict[cur]
        else:
            self.nums2_dict[cur] -= 1
        
        if new in self.nums2_dict:
            self.nums2_dict[new] += 1
        else:
            self.nums2_dict[new] = 1
        
        self.nums2[index] = new

    def count(self, tot: int) -> int:
        count = 0
        for num in self.nums1:
            other = tot - num
            count += self.nums2_dict.get(other, 0)
        return count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)